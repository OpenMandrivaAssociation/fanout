%define version 0.6.1
Summary:	Fanout lets you run commands on multiple remote machines simultaneously
Name:		fanout
Version:	%{version}
Release:	%mkrel 8
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




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-8mdv2011.0
+ Revision: 610419
- rebuild

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.6.1-7mdv2010.0
+ Revision: 437524
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6.1-6mdv2009.0
+ Revision: 245050
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.6.1-4mdv2008.1
+ Revision: 136408
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Mar 01 2007 Antoine Ginies <aginies@mandriva.com> 0.6.1-4mdv2007.0
+ Revision: 130586
- Import fanout

* Tue Aug 08 2006 Antoine Ginies <aginies@n3.mandriva.com> 0.6.1-4mdv2007.0
- use mkrel
- rebuild

* Mon Mar 21 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 0.6.1-3mdk
- rebuild

* Fri May 28 2004 <mdkc@n2.mandrakesoft.com> 0.6.1-2mdk
- add requires on xterm

* Thu May 27 2004 Aginies <mdkc@n2.mandrakesoft.com> 0.6.1-1mdk
- first release based on (William Stearns <wstearns@pobox.com> spec)

