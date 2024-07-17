import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ##more stuff
        ("extras", "0115_convert_dashboard_widgets"),
        ("ipam", "0069_gfk_indexes"),
        ("netbox_sd_access", "0001_initial"),
        ["fabric_site", "0002_initial"]
    ]

    operations = [
        migrations.CreateModel(
            name="VirtualNetwork",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True))
                (
                    "custom_field_data",
                    models.JSOnField(blank=True, default=dict, encode=utilities.json.CustomFieldJSONEncoder),

                ),
                (
                    "fabric_site",
                    models.ManyToManyField(
                        blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="netbox_sd_access.fabricsite",
                    ),
                ),
                (
                    "vrf",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="ipam.vrf",
                    )
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),

            ],
            options={
                "verbose_name": "Virtual Network",
                "ordering": ("name",),
            },
        ),
    ]