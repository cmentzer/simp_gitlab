# == Class simp_gitlab::config::firewall
#
# This class is meant to be called from simp_gitlab.
# It ensures that firewall rules are defined.
#
class simp_gitlab::config::firewall {
  assert_private()

  # FIXME: ensure yoour module's firewall settings are defined here.
  iptables::add_tcp_stateful_listen { 'allow_simp_gitlab_tcp_connections':
    client_nets => $::simp_gitlab::client_nets,
    dports      => $::simp_gitlab::tcp_listen_port,
  }

}
