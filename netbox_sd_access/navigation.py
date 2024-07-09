from netbox.plugins import PluginMenuButton, PluginMenuItem

fabricsite_buttons = [
    PluginMenuButton(
        link='plugins:netbox_sd_access:fabricsite_add',
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
        link='plugins:netbox_sd_access:ip_transits_list',
        link_text='IP Transits'
    ),
    PluginMenuItem(
        link='plugins:netbox_sd_access:sda_transits_list',
        link_text='SDA Transits'
    )
)
