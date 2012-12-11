%define	oname	Soya
%define	tutver	0.14

Summary:	A practical high-level object-oriented 3D engine
Name:		soya
Version:	0.14
Release:	6
License:	GPLv2+
Group:		Development/Python
Url:		http://home.gna.org/oomadness/en/index.html
Source0:	http://download.gna.org/soya/%{oname}-%{version}.tar.bz2
Source1:	http://download.gna.org/soya/%{oname}Tutorial-%{tutver}.tar.bz2
Patch0:		soya-0.14-glu.patch
BuildRequires:	python-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	SDL-devel
BuildRequires:	cal3d-devel
BuildRequires:	mesaglu-devel
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
python setup.py build #--dont-build-ode

%install
python setup.py install --root=%{buildroot}

%files
%doc README CHANGES AUTHORS
%{_bindir}/%{name}_editor
%{py_platsitedir}/%{name}
%{py_platsitedir}/*.egg-info

%files tutorial
%defattr(644,root,root,0755)
%doc %{oname}Tutorial-%{tutver}/AUTHORS %{oname}Tutorial-%{tutver}/tutorial


%changelog
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.14-5mdv2011.0
+ Revision: 590079
- rebuild for python 2.7

* Sun Apr 25 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.14-4mdv2010.1
+ Revision: 538541
- Fix installation with right requires

* Fri May 29 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.14-3mdv2010.0
+ Revision: 381032
- add suggests for soya-tutorial on blender, python-imaging & cerealizer (#35453)

* Sat Dec 27 2008 Michael Scherer <misc@mandriva.org> 0.14-2mdv2009.1
+ Revision: 319896
- rebuild for new python

* Sat Sep 06 2008 Emmanuel Andry <eandry@mandriva.org> 0.14-1mdv2009.0
+ Revision: 281880
- New version

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.13.2-1mdv2009.0
+ Revision: 140850
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 02 2007 Adam Williamson <awilliamson@mandriva.org> 0.13.2-1mdv2008.0
+ Revision: 57971
- drop patch1 (merged upstream)
- use py_platsitedir macro in both places in file list
- specify license as GPLv2
- new upstream release 0.13.2, includes fixes for python 2.5 (#32216)


* Sun Mar 11 2007 Olivier Blin <oblin@mandriva.com> 0.13-2mdv2007.1
+ Revision: 141199
- fix crash when loading models (patch from Jan Ciger, #27714)

  + Per Øyvind Karlsen <pkarlsen@mandriva.com>
    - update url

* Mon Feb 19 2007 Emmanuel Andry <eandry@mandriva.org> 0.13-1mdv2007.1
+ Revision: 122632
- New version 0.13
- This release supports latest ode (drop patch)

* Mon Jan 22 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.12-8mdv2007.1
+ Revision: 111645
- build against new ode

  + Olivier Blin <oblin@mandriva.com>
    - update buildrequires (pyrex is now named python-pyrex)

* Sat Dec 09 2006 Olivier Blin <oblin@mandriva.com> 0.12-7mdv2007.1
+ Revision: 94072
- use py_platsitedir for egg-info files
- include python egg-info files and rebuilt for new python (#27564)
- Import soya

* Wed Sep 27 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.12-6mdv2007.0
- I suck

* Wed Sep 27 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.12-5mdv2007.0
- bag one more buildrequires

* Wed Sep 27 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.12-4mdv2007.0
- build again now glew is really available

* Fri Sep 22 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.12-3mdv2007.0
- rebuild against new libcal3d (fixes #25814)

* Tue Aug 29 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.12-2mdv2007.0
- don't use included ode, but system ode (P0)
- cosmetics

* Mon Aug 28 2006 Emmanuel Andry <eandry@mandriva.org> 0.12-1mdv2007.0
- 0.12

* Sun Jun 18 2006 Emmanuel Andry <eandry@mandriva.org> 0.11.2-1mdv2007.0
- 0.11.2
- drop patch1
- fix buildrequires

* Wed Nov 30 2005 Guillaume Bedot <littletux@mandriva.org> 0.10.1-3mdk
- rebuild

* Tue Oct 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.10.1-2mdk
- Fix BuildRequires

* Wed Aug 31 2005 Michael Scherer <misc@mandriva.org> 0.10.1-1mdk
- update to 0.10.1
- rpmbuildupdateable

* Fri Apr 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.3-0.cvs20050313.3mdk
- update url
- %%mkrel
- build against new dynamically linked ode (P1)

* Tue Mar 15 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.3-0.cvs20050313.2mdk
- make it work with latest cal3d (P0 from Jan Ciger, fixes #14567)

* Mon Mar 14 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.3-0.cvs20050313.1mdk
- use cvs snapshot to work against latest cal3d

* Wed Mar 09 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.2-2mdk
- rebuild for new cal3d

* Tue Feb 08 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.9.2-1mdk
- from Gertz Raphaël <rapsys@free.fr> : 
- 0.9.2

* Thu Jan 20 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.1-3mdk
- fix buildrequires

* Fri Jan 14 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.1-2mdk
- fix buildrequires

* Mon Jan 03 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.1-1mdk
- 0.9.1
- updated tutorial to 0.9
- fix summary-ended-with-dot

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 0.8.2-2mdk
- Rebuild for new python

* Sat Oct 23 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.8.2-1mdk
- 0.8.2

* Fri Jul 09 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.7c-1mdk
- 0.7c
- drop patch, fixed upstream
- add new buildrequires
- update tutorial

* Wed Jun 30 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.6.1-4mdk
- update url

* Thu Jun 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.6.1-3mdk
- rebuild

