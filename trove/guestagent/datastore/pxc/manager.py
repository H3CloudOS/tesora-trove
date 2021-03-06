# Copyright 2015 Tesora, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from trove.guestagent.datastore.pxc import service as pxc_service
from trove.guestagent.datastore.galera_common import manager
from trove.guestagent.datastore.mysql_common import service as mysql_service


class Manager(manager.GaleraManager):

    def __init__(self):
        super(Manager, self).__init__(pxc_service.PXCApp,
                                      mysql_service.BaseMySqlAppStatus,
                                      pxc_service.PXCAdmin)
