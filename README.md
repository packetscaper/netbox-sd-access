# NetBox SD-Access Plugin

NetBox plugin for SD-Access.


* Documentation: https://theelliotm.github.io/netbox-sd-access/


## Features

The features the plugin provides should be listed here.

## Compatibility

| NetBox Version | Plugin Version |
|----------------|----------------|
|     4.0        |      0.1.0     |

## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

While this is still in development and not yet on pypi you can install with pip:

```bash
pip install git+https://github.com/theelliotm/netbox-sd-access
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
git+https://github.com/theelliotm/netbox-sd-access
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    'netbox-sd-access'
]

PLUGINS_CONFIG = {
    "netbox-sd-access": {},
}
```

## Developing

Development can be done using Docker and VS Code Dev Containers. Open the repository in VS Code and make sure you have the Dev Containers extension installed. Then use `Ctrl+Shift+P` (`Cmd+Shift+P` on Mac) and select "Dev Containers: Reopen in Container". When you are done, you can exit the Dev Container by clicking on the icon in the bottom left corner and selecting "Close Remote Connection". When you want to reopen the container, you can use the same steps, or simply select the workspace marked with \[Dev Container\] on VS Code.

To install the plugin, use `pip install --editable .` once the container loads, and then use `python ../manage.py migrate`

To run the server, use `python ../manage.py runserver`

### Testing

To test the plugin, run `python ../manage.py test netbox_sd_access` while inside the plugin directory in the dev container. Alternatively, you can run a specific test file by using `python ../manage.py test netbox_sd_access.tests.<test_file_name>` to run a specific test, such as `...test netbox_sd_access.tests.test_fabric_site`.

## Credits

Based on the NetBox plugin tutorial:

- [demo repository](https://github.com/netbox-community/netbox-plugin-demo)
- [tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`netbox-community/cookiecutter-netbox-plugin`](https://github.com/netbox-community/cookiecutter-netbox-plugin) project template.
