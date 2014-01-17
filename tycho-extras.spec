%{?_javapackages_macros:%_javapackages_macros}
# When building version under development (non-release)
# %%global snap -SNAPSHOT
%global snap %{nil}

Name:           tycho-extras
Version:        0.19.0
Release:        1.0%{?dist}
Summary:        Additional plugins for Tycho


License:        EPL
URL:            http://eclipse.org/tycho/
Source0:        http://git.eclipse.org/c/tycho/org.eclipse.tycho.extras.git/snapshot/tycho-extras-0.19.x.tar.bz2
Patch0:         %{name}-fix-build.patch
Patch1:         %{name}-use-custom-resolver.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  java-devel >= 1.5
BuildRequires:  jgit
BuildRequires:  tycho

Requires:       jpackage-utils
Requires:       java >= 1.5
Requires:       jgit
Requires:       tycho


%description
A small set of plugins that work with Tycho to provide additional functionality
when building projects of an OSGi nature.


%package javadoc
Summary:        Java docs for %{name}

Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n tycho-extras-0.19.x
%patch0 -p1
%patch1 -p1

# maven-properties-plugin is only needed for tests
%pom_remove_plugin org.eclipse.m2e:lifecycle-mapping
%pom_remove_plugin org.sonatype.plugins:maven-properties-plugin tycho-p2-extras-plugin
# remove org.apache.maven:apache-maven zip
%pom_remove_dep org.apache.maven:apache-maven tycho-p2-extras-plugin

%build
# To run tests, we need :
# maven-properties-plugin (unclear licensing)
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate

%install
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}

install -pm 644 pom.xml  %{buildroot}%{_mavenpomdir}/JPP.%{name}-main.pom
%add_maven_depmap JPP.%{name}-main.pom -a "org.eclipse.tycho:tycho-extras,org.sonatype.tycho:tycho-extras"

for mod in tycho-{custom-bundle,eclipserun,source-feature,version-bump}-plugin \
           tycho-{buildtimestamp,sourceref}-jgit tycho-p2-extras-plugin \
           pack200/tycho-pack200{{a,b}-plugin,-impl} \
           target-platform-validation-plugin ; do
   echo $mod
   aid=`basename $mod`
   install -pm 644 $mod/pom.xml  %{buildroot}%{_mavenpomdir}/JPP.%{name}-$aid.pom
   install -m 644 $mod/target/$aid-%{version}%{snap}.jar %{buildroot}%{_javadir}/%{name}/$aid.jar
   %add_maven_depmap JPP.%{name}-$aid.pom %{name}/$aid.jar -a "org.eclipse.tycho:$aid,org.sonatype.tycho:$aid"
done

for pommod in pack200; do
   echo $pommod
   aid=`basename $pommod`
   install -pm 644 $pommod/pom.xml  %{buildroot}%{_mavenpomdir}/JPP.%{name}-$aid.pom
   %add_maven_depmap JPP.%{name}-$aid.pom -a "org.eclipse.tycho:$aid,org.sonatype.tycho:$aid"
done

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Oct 25 2013 Roland Grunberg <rgrunber@redhat.com> - 0.19.0-1
- Update to 0.19.0 Release.

* Mon Jul 29 2013 Roland Grunberg <rgrunber@redhat.com> 0.18.1-1
- Update to 0.18.1 Release.

* Thu May 30 2013 Roland Grunberg <rgrunber@redhat.com> 0.18.0-1
- Update to 0.18.0 Release.

* Tue May 7 2013 Roland Grunberg <rgrunber@redhat.com> 0.17.0-2
- tycho-eclipserun-plugin should use the system local p2 repo.

* Tue Apr 2 2013 Roland Grunberg <rgrunber@redhat.com> 0.17.0-1
- Update to 0.17.0 Release.

* Mon Feb 25 2013 Roland Grunberg <rgrunber@redhat.com> 0.17.0-0.1.git0a9370
- Update to latest 0.17.0-SNAPSHOT.

* Thu Feb 21 2013 Roland Grunberg <rgrunber@redhat.com> - 0.16.0-5
- Fix PlexusConfiguration class issues identically across branches.

* Wed Feb 20 2013 Roland Grunberg <rgrunber@redhat.com> - 0.16.0-4
- Fix build issues relating to PlexusConfiguration.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-3
- Fix upstream Bug 393686.

* Fri Oct 19 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-2
- Update to 0.16.0 Release.

* Mon Jul 30 2012 Roland Grunberg <rgrunber@redhat.com> 0.16.0-1.e58861
- Update to 0.16.0 SNAPSHOT.

* Fri Jul 27 2012 Roland Grunberg <rgrunber@redhat.com> 0.15.0-1
- Update to 0.15.0.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Roland Grunberg <rgrunber@redhat.com> - 0.14.0-1
- Initial packaging of tycho extras.
