# == Class simp_gitlab::params
#
# This class is meant to be called from simp_gitlab.
# It sets variables according to platform.
#
class simp_gitlab::params {
  case $::osfamily {
    'RedHat': {
      $package_name = 'simp_gitlab'
      $service_name = 'simp_gitlab'
    }
    default: {
      fail("${::operatingsystem} not supported")
    }
  }
}
