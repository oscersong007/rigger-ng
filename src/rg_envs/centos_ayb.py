from setting import rgenv

def rgenv_enable() :
    rgenv['PHP_BIN']    = "/usr/local/php-5.6/bin/php"
    rgenv['PHP_INI']    = "/usr/local/php-5.6/lib/php.ini"
    rgenv['VARNISHD']   = "/usr/local/varnish-4.1.2/sbin/varnishd"
    rgenv['VARNISHADM'] = "/usr/local/lvarnish-4.1.2/bin/varnishadm"
    rgenv['RG_DEVPATH'] = "/data/${USER}/devspace/rigger-ng"

