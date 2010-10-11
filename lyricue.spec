
%include    /usr/lib/rpm/macros.perl

Summary:	GNU Lyric Display System, client interface
Name:		lyricue
Version:	3.0.10
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.lyricue.org/archive/%{name}_%{version}.tar.gz
# Source0-md5:	8544bb12dddef9f2176926a752e6e9df
URL:		http://www.lyricue.org
BuildRequires:	gettext-devel
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0
Requires:	mysql-client
Requires:	%{name}-display
Requires:	%{name}-remote
Requires:	perl-Gtk2 >= 1.220
Suggests:	diatheke
Suggests:	mysql
Suggests:	perl-DBD-mysql
Suggests:	perl-DBD-SQLite
Suggests:	perl-Gtk2-Spell
Suggests:	perl-Gtk2-TrayIcon
Suggests:	totem
Suggests:	unoconv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lyricue is used to edit and display song lyrics and passages of text
along with images and videos on a second screen/projector. It was
designed for use at live events such as church services, concerts and
seminars.

%package display
Summary:	GNU Lyric Display System, display interface
Group:		X11/Applications/Graphics
Obsoletes:	%{name}-server
Requires:	perl-Gtk2 >= 1.220
Suggests:	perl-DBD-mysql
Suggests:	perl-DBD-SQLite
Suggests:	perl-Locale-gettext
Suggests:	totem

%description display
Component to handle action display and projection of slides.

%package remote
Summary:	GNU Lyric Display System, remote control cli
Group:		Libraries

%description remote
Remote control CLI to control the projection display from any shell.

%prep
%setup -q

# Upstream package is missing ChangeLog file referenced in the Makefile
cp NEWS ChangeLog

# Fix perl shebang
%{__sed} -i -e '1s,^#!.*perl,#!%{__perl},' src/%{name} src/%{name}_remote

%build
%configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#rm -r $RPM_BUILD_ROOT%{_datadir}/doc

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_desktopdir}/%{name}.desktop

%files display
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}_display
%{_desktopdir}/%{name}_display.desktop

%files remote
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}_remote
