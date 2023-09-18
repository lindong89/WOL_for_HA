"""
Hass.io My Custom Switch Plugin Config Flow
"""
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

from homeassistant.components.http.view import HomeAssistantView
from aiohttp import web

@config_entries.HANDLERS.register(DOMAIN)
class MyCustomSwitchFlowHandler(config_entries.ConfigFlow):
    async def async_step_user(self, user_input=None):
        errors = {}
        if DOMAIN in self.hass.data:
            return self.async_abort(reason="single_instance_allowed")
        if user_input is not None:

            return self.async_create_entry(title="WOL_for_HA_Configuration", data=user_input)
        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({
                vol.Required("ip", default = ""): str,
                vol.Required("name", default = ""): str,
                vol.Required("mac", default = ""): str,
            })
        )

