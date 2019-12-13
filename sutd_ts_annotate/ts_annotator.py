
from pdf_annotate import PdfAnnotator, Location, Appearance
from pdf_annotate.util.validation import Color
from pdf_annotate.config.constants import BLACK

from sutd_ts_annotate.parameters import *
from datetime import datetime
from typing import Any, Dict
from copy import deepcopy
import subprocess


class TimesheetAnnotator:

    def __init__(self, filename: str, parameters: Dict[str, Any] = {}):

        self.ann: PdfAnnotator = PdfAnnotator(filename)

        values: Dict[str, Dict[str, Any]] = deepcopy(defaults)
        for category in values.values():
            for key, value in parameters.items():
                if key in category: category[key] = value
                
        for k, v in values['predefined'].items():
            self.write_predefined(k, v)

        vac = values['options']['vacation']
        for pos in term_vacation_params.values():
            self.draw_strike(*pos, vacation=vac)

        for k, v in values['checkboxes'].items():
            if v == False: continue
            self.draw_tick(*checkbox_params[k])


    def draw_strike(self, x: int, y:int, page: int, vacation: bool = False):
        '''Draws a verticle strike symbol.'''

        y_offset = 0 if vacation else 13
        y -= y_offset

        self.ann.add_annotation(
            'square', 
            Location(x1=x-20, y1=y, x2=x+40, y2=y, page=page),
            Appearance(stroke_color=(0, 0, 0), stroke_width=5)
        )

    def draw_tick(self, x: int, y:int, page: int):
        '''Draws a tick symbol.'''

        points = [(x-2, y-2), (x+4, y+4)]

        self.ann.add_annotation(
            'line', 
            Location(points=points, page=page),
            Appearance(stroke_color=(0, 0, 0), stroke_width=3)
        )

    def write_predefined(self, entry_type: str, content: str):
        '''Writes text onto a predefined location on the document.'''

        if entry_type not in text_params:
            raise IndexError('"{}" is an unknown type')

        args: Any = list(text_params[entry_type])
        args.insert(5, content)

        self.write(*args)

    def write_data(self, i: int, 
            date: str=None, start: str=None, end: str=None, 
            hours_total: int=None, breaks: int=None, 
            sub_total: int=None, job: str=None, supervisor: str=None):
        '''Writes data from a line of the table to the table.'''

        values = [date, start, end, hours_total, breaks, sub_total, job, supervisor]
        params = line_params.values()

        for v, (x, s) in zip(values, params):
            if v == None: continue
            self.write_on_table(x, i, str(v), size=s)


    def write_on_table(self, x: int, row: int, text: str, size: int=9):
        '''Write a single element of the table on the specified row.'''

        if row // 21 == 0:
            page = 0
            start_y = table_params['first_page']
        else:
            page = 1
            start_y = table_params['second_page']
            row %= 21

        row_height = table_params['row_height']
        row_y = start_y - row_height * row - row // 7 * 2

        self.write(x, row_y, 80, row_height, page, text, size)

    def write(self, x: int, y: int, w: int, h: int, page: int, content: str, size: int):
        '''Writes text onto the pdf document with the given parameters.'''

        self.ann.add_annotation(
            'text',
            Location(x1=x, y1=y, x2=x+w, y2=y-h, page=page),
            Appearance(content=str(content), fill=(0, 0, 0), font_size=size),
        )

    def output_to_file(self, filename: str, open_file: bool=False):
        '''Outputs the modified pdf to a file given a filename.'''

        self.ann.write(filename)
        if open_file:
            subprocess.run(['open', filename])








