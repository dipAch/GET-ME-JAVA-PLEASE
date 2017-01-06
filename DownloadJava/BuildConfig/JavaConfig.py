# Default constants for the generic installation of `JAVA` on production systems.
# Please alter the below configurations to suit your environment needs.
BASE_URL           = 'http://www.oracle.com'
JAVA_PACKAGE       = 'server-jre'
JAVA_VERSION       = 8
ARCHITECTURE_SET   = 'linux-x64'
PACKAGE_EXTENSION  = '.tar.gz'

# Locate the `JAVA::PACKAGE::DOWNLOADS` link from the Primary Oracle `JAVA` Downloads Page.
DOWNLOADS_URL      = BASE_URL + '/technetwork/java/javase/downloads/index.html'
DOWNLOAD_PATTERN   = '/technetwork/java/javase/downloads/' + JAVA_PACKAGE + str(JAVA_VERSION) + '-downloads-[0-9]+\.html'

# Download the "*.tar.gz" package for `JAVA`.
# Need to extract the link for the package download
# from the downloads page.
# Below are the identifier entities for doing that.
DOWNLOAD_TAR_PATTERN = 'http://download\.oracle\.com/otn-pub/java/jdk/[7-9]u([0-9]+)?-.+/' + JAVA_PACKAGE + \
						'-[7-9]u([0-9]+)?-' + ARCHITECTURE_SET + PACKAGE_EXTENSION