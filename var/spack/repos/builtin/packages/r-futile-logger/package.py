# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RFutileLogger(RPackage):
    """Provides a simple yet powerful logging utility. Based loosely on log4j,
       futile.logger takes advantage of R idioms to make logging a convenient
       and easy to use replacement for cat and print statements."""

    homepage = "https://cran.rstudio.com/web/packages/futile.logger/index.html"
    url      = "https://cran.rstudio.com/src/contrib/futile.logger_1.4.3.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/futile.logger"

    version('1.4.3', 'ba0e8d2dfb5a970b51c21907bbf8bfc2')

    depends_on('r-lambda-r', type=('build', 'run'))
    depends_on('r-futile-options', type=('build', 'run'))
