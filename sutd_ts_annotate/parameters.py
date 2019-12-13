from typing import Any, Dict, Tuple

defaults: Dict[str, Dict[str, Any]] = {

    'predefined': {

        'month': '',
        'year': '',
        'total_hours': 0,
        'total_wage': 0,
        'date': '',

        'name': '',
        'student_id': '',
        'contact_no': '',

    },

    'options': {

        'vacation': False

    },

    'checkboxes': {

        'terms_and_conditions': True,
        'internship': True,
        'leave_of_absense': True,

    }

}

text_params: Dict[str, Tuple[int, int, int, int, int, int]] = {

    # Format: x, y, w, h, page, font_size.

    'month': (100, 450, 300, 50, 0, 14),
    'year': (650, 450, 50, 50, 0, 14),
    'total_hours': (400, 338, 50, 50, 1, 9),
    'total_wage': (610, 338, 90, 50, 1, 9),
    'date': (640, 210, 50, 20, 1, 8),

    'name': (228, 207, 150, 20, 1, 8),
    'student_id': (228, 194, 150, 20, 1, 8),
    'contact_no': (575, 194, 150, 20, 1, 8)

}

table_params: Dict[str, int] = {

    # Format: title, y-value.

    'first_page': 336,
    'second_page': 519,
    'row_height': 14

}

line_params: Dict[str, Tuple[int, int]] = {

    # Format: title, x-value.

    'date': (102, 9),
    'start': (164, 9),
    'end': (218, 9),
    'breaks': (273, 9),
    'total_daily': (335, 9),
    'sub_total': (435, 9),
    'job': (575, 7),
    'supervisor': (660, 7)

}

term_vacation_params: Dict[int, Tuple[int, int, int]] = {

    # Format: x, y, page.

    1: (520, 293, 0),
    2: (520, 194, 0),
    3: (520, 95, 0),
    4: (520, 477, 1),
    5: (520, 377, 1),

}

checkbox_params: Dict[str, Tuple[int, int, int]] = {

    # Format: x, y, page.

    'terms_and_conditions': (20, 256, 1),
    'internship': (20, 240, 1),
    'leave_of_absense': (20, 224, 1),

}