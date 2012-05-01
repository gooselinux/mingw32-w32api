%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}
%global _use_internal_dependency_generator 0
%global __find_requires %{_mingw32_findrequires}
%global __find_provides %{_mingw32_findprovides}

Name:           mingw32-w32api
Version:        3.14
Release:        1%{?dist}.5
Summary:        Win32 header files and stubs


License:        Public Domain
Group:          Development/Libraries
URL:            http://www.mingw.org/
Source0:        http://downloads.sourceforge.net/mingw/w32api-%{version}-mingw32-src.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 49
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc >= 4.4.0
BuildRequires:  mingw32-runtime

Requires:       mingw32-runtime

# Once this is installed, mingw32-bootstrap (binary bootstrapper) is no
# longer needed.
Obsoletes:      mingw32-w32api-bootstrap


%description
MinGW Windows cross-compiler Win32 header files.


%prep
%setup -q -n w32api-%{version}-mingw32

%build
%{_mingw32_configure}
make


%install
rm -rf $RPM_BUILD_ROOT

%{_mingw32_makeinstall}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%{_mingw32_includedir}/*
%{_mingw32_libdir}/*.a


%changelog
* Mon Dec 27 2010 Andrew Beekhof <abeekhof@redhat.com> - 3.14-1.5
- Rebuild everything with gcc-4.4
  Related: rhbz#658833

* Fri Dec 24 2010 Andrew Beekhof <abeekhof@redhat.com> - 3.14-1.4
- Rebuild for new 3.18 mingw32 runtime
  Related: rhbz#658833

* Fri Dec 24 2010 Andrew Beekhof <abeekhof@redhat.com> - 3.14-1.3
- The use of ExclusiveArch conflicts with noarch, using an alternate COLLECTION to limit builds
  Related: rhbz#658833

* Wed Dec 22 2010 Andrew Beekhof <abeekhof@redhat.com> - 3.14-1.2
- Only build mingw packages on x86_64
  Related: rhbz#658833

* Wed Dec 22 2010 Andrew Beekhof <abeekhof@redhat.com> - 3.14-1.1
- Bump the revision to avoid tag collision
  Related: rhbz#658833

* Thu May 13 2010 Kalev Lember <kalev@smartlink.ee> - 3.14-1
- Updated to 3.14
- Replaced %%define with %%global

* Wed Jan 13 2010 Richard W.M. Jones <rjones@redhat.com> - 3.13-5
- Fix Source0 URL.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 3.13-2
- Rebuild for mingw32-gcc 4.4

* Mon Dec 15 2008 Richard W.M. Jones <rjones@redhat.com> - 3.13-1
- New upstream version 3.13.

* Tue Dec  9 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-8
- Force rebuild to get rid of the binary bootstrap package and replace
  with package built from source.

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-7
- No runtime dependency on binutils or gcc.

* Mon Nov 24 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-6
- Rebuild against latest filesystem package.
- Rewrite the summary for accuracy and brevity.

* Fri Nov 21 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-4
- Remove obsoletes for a long dead package.
- Enable _mingw32_configure (Levente Farkas).

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-3
- Rebuild against mingw32-filesystem 37

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-2
- Rebuild against mingw32-filesystem 36

* Thu Oct 16 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-1
- New upstream version 3.12.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 3.11-7
- Rename mingw -> mingw32.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 3.11-6
- Moved ole provides to mingw-filesystem package.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 3.11-3
- Use the RPM macros from mingw-filesystem.

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 3.11-2
- Initial RPM release, largely based on earlier work from several sources.
