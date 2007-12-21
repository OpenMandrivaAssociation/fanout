%define version 0.6.1
Summary:	Fanout lets you run commands on multiple remote machines simultaneously
Name:		fanout
Version:	%{version}
Release:	%mkrel 4
License:	GPL
Group:		Networking/Remote access
Source:		http://www.stearns.org/fanout/fanout-%{version}.tar.bz2
URL:		http://www.stearns.org/fanout/
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Buildarch:	noarch
requires:	xterm

%description
Fanout allows you to run non-interactive commands on remote
machines simultaneously, collecting the output in an organized fashion.

%prep
%setup
#%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
#%make DESTDIR=$RPM_BUILD_ROOT install
echo $RPM_BUILD_DIR
cp -avf $RPM_BUILD_DIR/%name-%version/fanout $RPM_BUILD_ROOT/%{_bindir}
cp -avf $RPM_BUILD_DIR/%name-%version/fanterm $RPM_BUILD_ROOT/%{_bindir}
cp -avf $RPM_BUILD_DIR/%name-%version/fanmux $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING CREDITS ChangeLog Makefile
%attr(755,root,root) %{_bindir}/fanmux
%attr(755,root,root) %{_bindir}/fanout
%attr(755,root,root) %{_bindir}/fanterm


