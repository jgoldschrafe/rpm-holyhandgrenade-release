Summary:   holyhandgrenade.org repo release files
Name:      holyhandgrenade-release
Version:   1.0
Release:   2%{?dist}
License:   GPL
Group:     System Environment/Base
Source0:   RPM-GPG-KEY-holyhandgrenade
Source2:   holyhandgrenade.repo
BuildArch: noarch

%description
holyhandgrenade.org repo release files

%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 644 %{SOURCE0} \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-holyhandgrenade

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/holyhandgrenade.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-holyhandgrenade

%changelog
* Mon Oct 10 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 1.0-2.hhg
- Enable GPG signature checking
- holyhandgrenade.repo file should be marked %config(noreplace)

* Tue Oct  4 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 1.0-1.hhg
- Initial release
