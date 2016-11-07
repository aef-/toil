# Copyright (C) 2015 UCSC Computational Genomics Lab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Terminates the specified cluster and associated resources
"""
import logging
from toil.lib.bioio import parseBasicOptions, setLoggingFromOptions
from toil.utils import getBasicProvisionerParser

logger = logging.getLogger( __name__ )


def main():
    parser = getBasicProvisionerParser()
    config = parseBasicOptions(parser)
    setLoggingFromOptions(config)
    if config.provisioner == 'aws':
        logger.info('Using aws provisioner.')
        try:
            from toil.provisioners.aws.awsProvisioner import AWSProvisioner
        except ImportError:
            raise RuntimeError('The aws extra must be installed to use this provisioner')
        provisioner = AWSProvisioner
    else:
        assert False

    provisioner.destroyCluster(clusterName=config.clusterName)