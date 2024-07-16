from netbox.plugins import PluginMenuButton, PluginMenuItem

fabricsite_buttons = [
    PluginMenuButton(
        link='plugins:netbox_sd_access:fabricsite_add',
        title='Add',
        icon_class='mdi mdi-plus-thick'
    ),
]

virtualnetwork_buttons = [
    PluginMenuButton(
        link='plugins:netbox_sd_access:virtualnetwork_list',
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
        link='plugins:netbox_sd_access:virtualnetwork_list',
        link_text='Virtual Networks',
        buttons=virtualnetwork_buttons
    ),
)