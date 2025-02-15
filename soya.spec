%define	oname	Soya
%define	tutver	0.14

Summary:	A practical high-level object-oriented 3D engine
Name:		soya
Version:	0.14
Release:	9
License:	GPLv2+
Group:		Development/Python
Url:		https://home.gna.org/oomadness/en/index.html
Source0:	http://download.gna.org/soya/%{oname}-%{version}.tar.bz2
Source1:	http://download.gna.org/soya/%{oname}Tutorial-%{tutver}.tar.bz2
Patch0:		soya-0.14-glu.patch
# Python 3 does not support string exceptions
BuildRequires:	python2-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	cal3d-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	ode-devel
BuildRequires:	glew-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	openal-devel
Requires:	editobj2

%description
A practical high-level object-oriented 3D engine.

# (jiba) A separate package for the tutorial
%package	tutorial
Summary:	Tutorial for the Soya 3D engine
License:	GPLv2+
Group:		Development/Python
Requires:	%{name} >= %{version}
Suggests:	blender python-imaging cerealizer

%description	tutorial
This is a set of tutorial for Soya.
Soya is a practical high-level object-oriented 3D engine for Python.

%prep
%setup -q -n %{oname}-%{version} -a 1
%patch0 -p0

rm -rf `find -name CVS` `find -name .cvswrappers`

%build
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH

python2 setup.py build 

%install
python2 setup.py install --root=%{buildroot}

%files
%doc README CHANGES AUTHORS
%{_bindir}/%{name}_editor
%{py2_platsitedir}/%{name}
%{py2_platsitedir}/*.egg-info

%files tutorial
%doc %{oname}Tutorial-%{tutver}/AUTHORS %{oname}Tutorial-%{tutver}/tutorial


