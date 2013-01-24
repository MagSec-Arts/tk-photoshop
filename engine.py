#
# Copyright (c) 2013 Shotgun Software, Inc
# ----------------------------------------------------
#
"""
A Photoshop engine for Tank.
"""

import logging
import tank
from tk_photoshop import photoshop


###############################################################################################
# The Tank Photoshop engine

class PhotoshopEngine(tank.platform.Engine):
    _logger = logging.getLogger('tank.photoshop.engine')

    ##########################################################################################
    # init and destroy
    def init_engine(self):
        self._init_logging()
        self.log_debug("%s: Initializing...", self)
        self.log_debug("photoshop module: %s", photoshop)

    def post_app_init(self):
        import tk_photoshop
        self._panel_generator = tk_photoshop.PanelGenerator(self)
        self._panel_generator.populate_panel()

    def destroy_engine(self):
        self.log_debug("%s: Destroying...", self)
        self._panel_generator.destroy_panel()

    ##########################################################################################
    # logging

    def _init_logging(self):
        if self.get_setting("debug_logging", False):
            self._logger.setLevel(logging.DEBUG)
        else:
            self._logger.setLevel(logging.INFO)

    def log_debug(self, msg, *args, **kwargs):
        self._logger.debug(msg, *args, **kwargs)

    def log_info(self, msg, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)

    def log_warning(self, msg, *args, **kwargs):
        self._logger.warning(msg, *args, **kwargs)

    def log_error(self, msg, *args, **kwargs):
        self._logger.error(msg, *args, **kwargs)

    def log_exception(self, msg, *args, **kwargs):
        self._logger.exception(msg, *args, **kwargs)
