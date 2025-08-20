# coding=utf-8
from __future__ import print_function

import argparse

from chat_completions_conversation import ChatCompletionsConversation
from get_unicode_multiline_input_with_editor import get_unicode_multiline_input_with_editor
from textcompat import filesystem_str_to_text, text_to_uri_str
from typing import Optional, Text


def generate_google_calendar_event_url(
        title,  # type: Text
        start_datetime,  # type: Text
        end_datetime,  # type: Text
        description=None,  # type: Optional[Text]
        location=None,  # type: Optional[Text]
        iana_timezone_name=None  # type: Optional[Text]
):  # type: (...) -> Text
    unicode_base_url = u'https://calendar.google.com/calendar/render'

    unicode_query_string_fragments = [
        u'action=TEMPLATE',
        u'text=%s' % text_to_uri_str(title),
        u'dates=%s/%s' % (start_datetime, end_datetime)
    ]

    if description is not None:
        unicode_query_string_fragments.append(u'details=%s' % text_to_uri_str(description))

    if location is not None:
        unicode_query_string_fragments.append(u'location=%s' % text_to_uri_str(location))

    if iana_timezone_name is not None:
        unicode_query_string_fragments.append(u'ctz=%s' % text_to_uri_str(iana_timezone_name))

    unicode_query_string = u'&'.join(unicode_query_string_fragments)

    return u'%s?%s' % (unicode_base_url, unicode_query_string)


def main():
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument('--api-key', type=str, required=True, help='API key')
    parser.add_argument('--base-url', type=str, required=True, help='Base URL')
    parser.add_argument('--model', type=str, required=True, help='Model name')

    # Parse arguments
    args = parser.parse_args()

    # Initialize conversation
    conversation = ChatCompletionsConversation(
        api_key=filesystem_str_to_text(args.api_key),
        base_url=filesystem_str_to_text(args.base_url),
        model=filesystem_str_to_text(args.model)
    )

    event_natural_language_description = u''.join(
        get_unicode_multiline_input_with_editor(
            [
                u'# Enter natural language description of event above.',
                u'# Lines starting with # will be ignored.'
            ],
            u'#'
        )
    )
    conversation.append_user_message(event_natural_language_description)

    def prompt_and_correct(what):
        # type: (Text) -> Text
        print(u'\nModel-generated %s: ' % what, end=u'')

        response_fragments = []
        print(u"'''", end=u'')
        for chunk in conversation.send_and_stream_response(u'%s: ' % what):
            response_fragments.append(chunk)
            print(chunk, end=u'')
        model_generated = u''.join(response_fragments)
        print(u"'''")

        corrected = u''.join(
            get_unicode_multiline_input_with_editor(
                [
                    model_generated,
                    u'# Edit model-generated %s above.' % what,
                    u'# Lines starting with # will be ignored.'
                ],
                u'#'
            )
        ).strip()

        print(u'\nCorrected %s: ' % what, end=u'')
        print(u"'''", end=u'')
        print(corrected, end=u'')
        print(u"'''")

        conversation.correct_last_response(corrected)

        return corrected

    event_title = prompt_and_correct(u'event title')
    start_datetime = prompt_and_correct(u'start datetime (YYYYMMDDTHHMMSS)')
    end_datetime = prompt_and_correct(u'end datetime (YYYYMMDDTHHMMSS)')
    event_description = prompt_and_correct(u'event description')
    event_location = prompt_and_correct(u'event location')

    unicode_google_calendar_event_url = generate_google_calendar_event_url(
        title=event_title,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
        description=event_description,
        location=event_location
    )

    print(u'\nGenerated Google Calendar Event URL: ', end=u'')
    print(unicode_google_calendar_event_url)


if __name__ == '__main__':
    main()
