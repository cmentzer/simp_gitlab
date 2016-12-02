Summary: This module manages the gitlab community module for simp
Name: pupmod-simp_gitlab
Version: 0.1.0
Release: 0
License: Apache 2.0
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: pupmod-iptables >= 2.0.0-0
Requires: pupmod-simplib  >= 1.0.0-0
Requires: puppet >= 3.3.0
Buildarch: noarch

Prefix: %{_sysconfdir}/puppet/environments/simp/modules

%description
This module manages the gitlab community module for simp

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/simp_gitlab

dirs='files lib manifests templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/simp_gitlab
done

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/simp_gitlab

%files
%defattr(0640,root,puppet,0750)
%{prefix}/simp_gitlab

%post
#!/bin/sh

%postun
# Post uninstall stuff

%changelog
* Fri Dec 02 2016 Clay - 0.1.0-0
- Initial package.
