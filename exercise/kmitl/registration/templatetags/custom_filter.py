from django import template

register = template.Library()

@register.filter
def sortSectionByDayOfWeek(sections):
    for section in sections:
        section.day_of_week_num = section.dayOfWeek()
    return sections

@register.filter
def changePhone(number):
    first = number[:3]
    sec = number[3:6]
    last = number[6:]
    return f"{first}-{sec}-{last}"
