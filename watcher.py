"""Change the active window background on focus change."""

import logging
import sys
import traceback
from typing import Any

from kitty.window import DynamicColor, Window

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)-8s - %(message)s',
    filename='/tmp/kitty-watcher.log',
)
log = logging.getLogger(__name__)

log.info('Watcher started')

BG_COLOR_CODE = 11


def exception_handler(type, value, tb):
    _err = traceback.format_exception(type, value, tb)
    log.exception(''.join(_err))


sys.excepthook = exception_handler
log.info('Exception handler set')


def on_focus_change(boss: Any, window: Window, data: dict[str, Any]) -> None:
    log.debug(f'Focus change on {window.id}: {data}')
    _ = boss
    if data['focused']:
        log.debug(f'Window: {window.id} focused')
        window.set_dynamic_color(BG_COLOR_CODE, '#1c1c1c')
    else:
        log.debug(f'Window: {window.id} unfocused')
        window.set_dynamic_color(BG_COLOR_CODE, '#262626')
