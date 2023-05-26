from nicegui import ui

from ..documentation_tools import text_demo


def main_demo() -> None:
    from datetime import datetime

    label = ui.label()
    ui.timer(1.0, lambda: label.set_text(f'{datetime.now():%X}'))


def more() -> None:
    @text_demo('Activate and deactivate a timer', '''
        You can activate and deactivate a timer using the `active` property.
    ''')
    def activate_deactivate_demo():
        slider = ui.slider(min=-1, max=1, value=0)
        timer = ui.timer(0.1, lambda: slider.set_value((slider.value + 0.01) % 1.0))
        ui.switch('active').bind_value_to(timer, 'active')

    @text_demo('Call a function after a delay', '''
        You can call a function after a delay using a timer with the `once` parameter.
    ''')
    def call_after_delay_demo():
        def handle_click():
            ui.timer(1.0, lambda: ui.notify('Hi!'), once=True)
        ui.button('Notify after 1 second', on_click=handle_click)
