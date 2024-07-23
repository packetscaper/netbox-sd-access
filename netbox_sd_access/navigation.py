from netbox.plugins import PluginMenuButton, PluginMenuItem

fabricsite_buttons = [
    PluginMenuButton(
        link='plugins:netbox_sd_access:fabricsite_add',
        title='Add',
        icon_class='mdi mdi-plus-thick'
    ),
    PluginMenuButton(
        link='plugins:netbox_sd_access:fabricsite_import',
        title='Import',
        icon_class='mdi mdi-upload',
    )
]

virtualnetwork_buttons = [
    PluginMenuButton(
        link='plugins:netbox_sd_access:virtualnetwork_add',
        title='Add',
        icon_class='mdi mdi-plus-thick'
    ),
]

devicerole_buttons = [
    PluginMenuButton(
        link='plugins:netbox_sd_access:sdadevice_add',
        title='Add',
        icon_class='mdi mdi-plus-thick'
    ),
    PluginMenuButton(
        link='plugins:netbox_sd_access:sdadevice_import',
        title='Import',
        icon_class='mdi mdi-upload',
    )
]

ip_transit_buttons = [
    PluginMenuButton(
        link='plugins:netbox_sd_access:iptransit_add',
        title='Add',
        icon_class='mdi mdi-plus-thick'
    ),
    PluginMenuButton(
        link='plugins:netbox_sd_access:iptransit_import',
        title='Import',
        icon_class='mdi mdi-upload',
    )
]

ippool_buttons = [
    PluginMenuButton(
        link='plugins:netbox_sd_access:ippool_add',
        title='Add',
        icon_class='mdi mdi-plus-thick'
    ),
]

sda_transit_buttons = [
    PluginMenuButton(
        link='plugins:netbox_sd_access:sdatransit_add',
        title='Add',
        icon_class='mdi mdi-plus-thick'
    ),
    PluginMenuButton(
        link='plugins:netbox_sd_access:sdatransit_import',
        title='Import',
        icon_class='mdi mdi-upload',
    )
]


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_sd_access:fabricsite_list',
        link_text='Fabric Sites',
        buttons=fabricsite_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_sd_access:sdadevice_list',
        link_text='SDA Devices',
        buttons=devicerole_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_sd_access:sdatransit_list',
        link_text='SDA Transits',
        buttons=sda_transit_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_sd_access:iptransit_list',
        link_text='IP Transits',
        buttons=ip_transit_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_sd_access:ippool_list',
        link_text='IP Pools',
        buttons=ippool_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_sd_access:virtualnetwork_list',
        link_text='Virtual Networks',
        buttons=virtualnetwork_buttons
    ),
)
