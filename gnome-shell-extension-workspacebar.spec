%define		extname		workspacebar
Summary:	A toolbar for your panel that allows you to switch workspaces
Name:		gnome-shell-extension-%{extname}
Version:	20121027
Release:	2
License:	GPL v2
Group:		X11/Applications
# $ git clone git://github.com/mbokil/workspacebar.git
# $ cd workspacebar/
# $ git archive --format=tar --prefix=%{name}-%{version}/ master | xz > ../%{name}-%{version}.tar.xz
Source0:	%{extname}-%{version}.tar.xz
# Source0-md5:	17535842481ad8d699c977eff06345af
Patch0:		no-undeclared.patch
URL:		http://markbokil.com/downloads/extensions/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gnome-shell >= 3.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A toolbar for your panel that allows you to switch workspaces. Latest
update includes a panel position option of left, center, and right.
Also there is an option to display the Overview on mouse entry.

%prep
%setup -q -n %{extname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas \
	$RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/workspace-bar@markbokil.com

cp -p schemas/org.gnome.shell.extensions.workspacebar.gschema.xml $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
cp -p *.js* $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/workspace-bar@markbokil.com
cp -p *.css $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/workspace-bar@markbokil.com

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.workspacebar.gschema.xml
%{_datadir}/gnome-shell/extensions/workspace-bar*
