# sutd-timesheet-annotator

A Python module to help with annotating SUTD Students@Part-Time Work Scheme timesheets.
Ever thought that filling out your SUTD Students@Part-Time Work Scheme timesheet was not a very fun or fufilling experience? Well do we have the module for you! 

You can now fill in your SUTD Students@Part-Time Work Scheme with (almost) zero hassle! With this you can stop worrying about filling up your SUTD Students@Part-Time Work Scheme, and focus on more important things - such as passing finals, or writing pointless modules that no one else will probably use!




## Example usage

```python
from sutd_ts_annotate import TimesheetAnnotator

template_path = './template.pdf'
options = {
    'month': 'January',
    'year': 2020,
    'name': 'Alice',
    'student_id': '1000000',
    'contact_no': '97653210'
}

annotator = TimesheetAnnotator(template_path, parameters=options)
annotator.write_data(4, '01/01/2020', '1400', '1600', 2, 0, None, 'Research Assistant', 'Bob')
annotator.write_data(5, '02/01/2020', '0800', '1800', 10, 2, None, 'Usher', 'Eve')

annotator.output_to_file('January.pdf', open_file=True)
```




## Writing data to the table

The easiest way to write data to the table is to use `write_data`, which takes in arguments according to each column of the table. Namely:

```
(i, date, start, end, hours_total, breaks, sub_total, job, supervisor)
```

| Argument      | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| *i*           | The row index of the table to write to.                      |
| *date*        | The date of the entry.                                       |
| *start*       | The starting time (in 24-hr represnetation) of the work.     |
| *end*         | The ending time (in 24-hr represnetation) of the work.       |
| *hours_total* | The total number of hours worked in that day.                |
| *breaks*      | The total hours of breaks taken in that day.                 |
| *sub_total*   | The subtotal of the week (should only be on the last day of every week). |
| *job*         | The job title of the entry.                                  |
| *supervisor*  | The supervisor of the job.                                   |



#### Examples

```python
annotator.write_data(4, '01/01/2020', '1400', '1600', 2, 0, None, 'Research Assistant', 'Bob')

annotator.write_data(5, '02/01/2020', '0800', '1800', 10, 2, None, 'Usher', 'Eve')

annotator.write_data(6, None, None, None, None, None, 12, None, None)

```




## Options

Almost every blank on the form can be written on through passing its key into the `parameters` argument.

```python
'options': {
  
  	# representing the blanks before the table.
    'month': 'January',
    'year': '',
  
  	# representing the blanks at the end of the table.
    'total_hours': 0,
    'total_wage': 0,

  	# representing the blanks after the table.
    'name': '',
    'student_id': '',
    'contact_no': '',
    'date': '',

  	# representing whether the 'term' or 'vacation' will be striked off.
    'vacation': False,

  	# Representing whether the checkboxes at the bottom will be checked.
    'terms_and_condition': True,
    'internship': True,
    'leave_of_absense': True, 
  
}
```



