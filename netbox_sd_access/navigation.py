from netbox.plugins import PluginMenuButton, PluginMenuItem

fabricsite_buttons = [
    PluginMenuButton(
        link='plugins:netbox_sd_access:fabricsite_add',
        title='Add',
        icon_class='mdi mdi-plus-thick'
    ),
]

devicerole_buttons = [
    PluginMenuButton(
        link='plugins:netbox_sd_access:sdadevicerole_add',
        title='Add',
        icon_class='mdi mdi-plus-thick'
    ),
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_sd_access:fabricsite_list',
        link_text='Fabric Sites',
        buttons=fabricsite_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_sd_access:sdadevicerole_list',
        link_text='Device Roles',
        buttons=devicerole_buttons
    ),
)
