from mistral_common.protocol.instruct.tool_calls import Function, Tool

create_event_tool = Tool(
    function=Function(
        name="create_event",
        description="Create a Google Calendar event",
        parameters={
            "type": "object",
            "properties": {
                "event_title": {
                    "type": "string",
                    "description": "The title of the event",
                },
                "emails": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The emails of the attendees",
                },
                "start": {
                    "type": "string",
                    "description": "The exact start date and time of the event in ISO 8601 format (e.g., '2024-06-12T14:00:00')",
                },
                "end": {
                    "type": "string",
                    "description": "The exact end date and time of the event in ISO 8601 format (e.g., '2024-06-12T14:00:00')",
                },
            },
            "required": ["event_title", "emails", "start", "end"],
        },
    )
)


free_busy_schedule_tool = Tool(
    function=Function(
        name="free_busy_schedule",
        description="Checking if the person is available or not.",
        parameters={
            "type": "object",
            "properties": {
                "emails": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The emails of the persons",
                },
                "time_min": {
                    "type": "string",
                    "description": "Start point of the time (optional)",
                },
                "time_max": {
                    "type": "string",
                    "description": "End point of the time (optional)",
                },
            },
            "required": ["emails"],
        },
    )
)

cancel_event_tool = Tool(
    function=Function(
        name="cancel_event",
        description="Cancel an event or meeting from the Google Calendar for a specific period of time or the whole day.",
        parameters={
            "type": "object",
            "properties": {
                "start_date": {
                    "type": "string",
                    "description": "The start date or start date with time of the event",
                },
                "end_date": {
                    "type": "string",
                    "description": "The end date or end date with time of the event (optional)",
                },
            },
            "required": ["start_date"],
        },
    )
)
list_events_tool = Tool(
    function=Function(
        name="list_events",
        description="List the events present in the Google Calendar for the provided email.",
        parameters={
            "type": "object",
            "properties": {
                "start_date": {
                    "type": "string",
                    "description": "The start date or start date with time of the event",
                },
                "end_date": {
                    "type": "string",
                    "description": "The end date or end date with time of the event(optional)",
                },
            },
            "required": ["start_date"],
        },
    )
)
