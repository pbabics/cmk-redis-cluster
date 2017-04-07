#!/usr/bin/python
#
# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 3.  This test is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.
# This configures the queue size/consumers limits in WATO.
#
group = "Applications, Processes & Services"

# def register_check_parameters(subgroup, checkgroup, title, valuespec, itemspec, matchtype, has_inventory=True, register_static_check=True):
#
register_check_parameters(
    group,
    "redis_cluster_state",
    _("Redis cluster status"),
    Dictionary(
        elements = [
            ("pfailInstances",
            Tuple(
               title = _("Levels for the number of partially failed slots"),
               help = _("Number of partially failed slots is a number of slots (parts of keyspace) that are currently unaccessible but can be recovered by failover"),
               elements = [
                  Integer(title="Warning more than", default_value=99999),
                  Integer(title="Critical more than", default_value=99999),
               ]
            )),
            ("failInstances",
            Tuple(
               title = _("Levels for the number of failed slots"),
               help = _("Number of failed slots is a number of unaccessible slots (parts of keyspace)"),
               elements = [
                  Integer(title="Warning more than", default_value=99999),
                  Integer(title="Critical more than", default_value=99999),
               ]
            )),
            ("unwantedFlags",
            Tuple(
               title = _("Unwated flags for node"),
               help = _("Flags that are unwanted for nodes (see redis documentation for list)"),
               elements = [
                  TextAscii(title="Warning if node contains one or more of these flags", default_value="pfail"),
                  TextAscii(title="Critical if node contains one or more of these flags", default_value="fail"),
               ]
            )),
        ]
    ),
    TextAscii( title=_("Cluster node address"),
    help=_("Address of redis cluster node")),
    "dict",
)
