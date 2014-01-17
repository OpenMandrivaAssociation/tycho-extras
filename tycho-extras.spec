
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		tycho-extras
Version:	0.19.0
Release:	1.0
License:	GPLv3+
Source0:	tycho-extras-0.19.0-1.0-omv2014.0.noarch.rpm
Source1:	tycho-extras-javadoc-0.19.0-1.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/tycho-extras
BuildArch:	noarch
Summary:	tycho-extras bootstrap version
Requires:	javapackages-bootstrap
Requires:	java >= 1.5
Requires:	jgit
Requires:	jpackage-utils
Requires:	tycho
Provides:	mvn(org.eclipse.tycho.extras:target-platform-validation-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-buildtimestamp-jgit) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-custom-bundle-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-eclipserun-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-extras) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-extras:pom:) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-p2-extras-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-pack200) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-pack200-impl) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-pack200:pom:) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-pack200a-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-pack200b-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-source-feature-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-sourceref-jgit) = 0.19.0
Provides:	mvn(org.eclipse.tycho.extras:tycho-version-bump-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho:pack200) = 0.19.0
Provides:	mvn(org.eclipse.tycho:pack200:pom:) = 0.19.0
Provides:	mvn(org.eclipse.tycho:target-platform-validation-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-buildtimestamp-jgit) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-custom-bundle-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-eclipserun-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-extras) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-extras:pom:) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-p2-extras-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-pack200-impl) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-pack200a-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-pack200b-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-source-feature-plugin) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-sourceref-jgit) = 0.19.0
Provides:	mvn(org.eclipse.tycho:tycho-version-bump-plugin) = 0.19.0
Provides:	mvn(org.sonatype.tycho:pack200) = 0.19.0
Provides:	mvn(org.sonatype.tycho:pack200:pom:) = 0.19.0
Provides:	mvn(org.sonatype.tycho:target-platform-validation-plugin) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-buildtimestamp-jgit) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-custom-bundle-plugin) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-eclipserun-plugin) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-extras) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-extras:pom:) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-p2-extras-plugin) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-pack200-impl) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-pack200a-plugin) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-pack200b-plugin) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-source-feature-plugin) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-sourceref-jgit) = 0.19.0
Provides:	mvn(org.sonatype.tycho:tycho-version-bump-plugin) = 0.19.0
Provides:	tycho-extras = 0.19.0-1.0:2014.0

%description
tycho-extras bootstrap version.

%files
/usr/share/java/tycho-extras
/usr/share/java/tycho-extras/target-platform-validation-plugin.jar
/usr/share/java/tycho-extras/tycho-buildtimestamp-jgit.jar
/usr/share/java/tycho-extras/tycho-custom-bundle-plugin.jar
/usr/share/java/tycho-extras/tycho-eclipserun-plugin.jar
/usr/share/java/tycho-extras/tycho-p2-extras-plugin.jar
/usr/share/java/tycho-extras/tycho-pack200-impl.jar
/usr/share/java/tycho-extras/tycho-pack200a-plugin.jar
/usr/share/java/tycho-extras/tycho-pack200b-plugin.jar
/usr/share/java/tycho-extras/tycho-source-feature-plugin.jar
/usr/share/java/tycho-extras/tycho-sourceref-jgit.jar
/usr/share/java/tycho-extras/tycho-version-bump-plugin.jar
/usr/share/maven-fragments/tycho-extras
/usr/share/maven-poms/JPP.tycho-extras-main.pom
/usr/share/maven-poms/JPP.tycho-extras-pack200.pom
/usr/share/maven-poms/JPP.tycho-extras-target-platform-validation-plugin.pom
/usr/share/maven-poms/JPP.tycho-extras-tycho-buildtimestamp-jgit.pom
/usr/share/maven-poms/JPP.tycho-extras-tycho-custom-bundle-plugin.pom
/usr/share/maven-poms/JPP.tycho-extras-tycho-eclipserun-plugin.pom
/usr/share/maven-poms/JPP.tycho-extras-tycho-p2-extras-plugin.pom
/usr/share/maven-poms/JPP.tycho-extras-tycho-pack200-impl.pom
/usr/share/maven-poms/JPP.tycho-extras-tycho-pack200a-plugin.pom
/usr/share/maven-poms/JPP.tycho-extras-tycho-pack200b-plugin.pom
/usr/share/maven-poms/JPP.tycho-extras-tycho-source-feature-plugin.pom
/usr/share/maven-poms/JPP.tycho-extras-tycho-sourceref-jgit.pom
/usr/share/maven-poms/JPP.tycho-extras-tycho-version-bump-plugin.pom

#------------------------------------------------------------------------
%package	-n tycho-extras-javadoc
Version:	0.19.0
Release:	1.0
Summary:	tycho-extras-javadoc bootstrap version
Requires:	javapackages-bootstrap
Requires:	jpackage-utils
Provides:	tycho-extras-javadoc = 0.19.0-1.0:2014.0

%description	-n tycho-extras-javadoc
tycho-extras-javadoc bootstrap version.

%files		-n tycho-extras-javadoc
/usr/share/javadoc/tycho-extras
/usr/share/javadoc/tycho-extras/allclasses-frame.html
/usr/share/javadoc/tycho-extras/allclasses-noframe.html
/usr/share/javadoc/tycho-extras/constant-values.html
/usr/share/javadoc/tycho-extras/deprecated-list.html
/usr/share/javadoc/tycho-extras/help-doc.html
/usr/share/javadoc/tycho-extras/index-all.html
/usr/share/javadoc/tycho-extras/index.html
/usr/share/javadoc/tycho-extras/org
/usr/share/javadoc/tycho-extras/org/eclipse
/usr/share/javadoc/tycho-extras/org/eclipse/tycho
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/buildtimestamp
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/buildtimestamp/jgit
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/buildtimestamp/jgit/JGitBuildTimestampProvider.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/buildtimestamp/jgit/PathFilter.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/buildtimestamp/jgit/class-use
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/buildtimestamp/jgit/class-use/JGitBuildTimestampProvider.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/buildtimestamp/jgit/class-use/PathFilter.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/buildtimestamp/jgit/package-frame.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/buildtimestamp/jgit/package-summary.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/buildtimestamp/jgit/package-tree.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/buildtimestamp/jgit/package-use.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/custombundle
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/custombundle/CustomBundleMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/custombundle/CustomBundleP2MetadataProvider.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/custombundle/class-use
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/custombundle/class-use/CustomBundleMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/custombundle/class-use/CustomBundleP2MetadataProvider.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/custombundle/package-frame.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/custombundle/package-summary.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/custombundle/package-tree.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/custombundle/package-use.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/eclipserun
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/eclipserun/EclipseRunMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/eclipserun/class-use
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/eclipserun/class-use/EclipseRunMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/eclipserun/package-frame.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/eclipserun/package-summary.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/eclipserun/package-tree.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/eclipserun/package-use.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/EclipseInf.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/ForkedPack200Wrapper.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/Pack200Archiver.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/Pack200Wrapper.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/class-use
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/class-use/EclipseInf.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/class-use/ForkedPack200Wrapper.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/class-use/Pack200Archiver.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/class-use/Pack200Wrapper.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/mojo
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/mojo/Pack200NormalizeMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/mojo/Pack200PackMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/mojo/class-use
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/mojo/class-use/Pack200NormalizeMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/mojo/class-use/Pack200PackMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/mojo/package-frame.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/mojo/package-summary.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/mojo/package-tree.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/mojo/package-use.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/package-frame.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/package-summary.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/package-tree.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/pack200/package-use.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourcefeature
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourcefeature/SourceFeatureMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourcefeature/SourceFeatureP2MetadataProvider.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourcefeature/class-use
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourcefeature/class-use/SourceFeatureMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourcefeature/class-use/SourceFeatureP2MetadataProvider.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourcefeature/package-frame.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourcefeature/package-summary.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourcefeature/package-tree.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourcefeature/package-use.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourceref
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourceref/jgit
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourceref/jgit/JGitSourceReferencesProvider.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourceref/jgit/class-use
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourceref/jgit/class-use/JGitSourceReferencesProvider.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourceref/jgit/package-frame.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourceref/jgit/package-summary.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourceref/jgit/package-tree.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/sourceref/jgit/package-use.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/tpvalidator
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/tpvalidator/TPError.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/tpvalidator/TPValidationMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/tpvalidator/class-use
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/tpvalidator/class-use/TPError.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/tpvalidator/class-use/TPValidationMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/tpvalidator/package-frame.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/tpvalidator/package-summary.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/tpvalidator/package-tree.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/extras/tpvalidator/package-use.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/Iu.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/MirrorMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/PublishFeaturesAndBundlesMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/Query.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/Repository.Layout.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/Repository.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/class-use
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/class-use/Iu.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/class-use/MirrorMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/class-use/PublishFeaturesAndBundlesMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/class-use/Query.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/class-use/Repository.Layout.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/class-use/Repository.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/package-frame.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/package-summary.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/package-tree.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/plugins/p2/extras/package-use.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump/AbstractUpdateMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump/UpdateProductMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump/UpdateTargetMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump/class-use
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump/class-use/AbstractUpdateMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump/class-use/UpdateProductMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump/class-use/UpdateTargetMojo.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump/package-frame.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump/package-summary.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump/package-tree.html
/usr/share/javadoc/tycho-extras/org/eclipse/tycho/versionbump/package-use.html
/usr/share/javadoc/tycho-extras/overview-frame.html
/usr/share/javadoc/tycho-extras/overview-summary.html
/usr/share/javadoc/tycho-extras/overview-tree.html
/usr/share/javadoc/tycho-extras/package-list
/usr/share/javadoc/tycho-extras/resources
/usr/share/javadoc/tycho-extras/resources/background.gif
/usr/share/javadoc/tycho-extras/resources/tab.gif
/usr/share/javadoc/tycho-extras/resources/titlebar.gif
/usr/share/javadoc/tycho-extras/resources/titlebar_end.gif
/usr/share/javadoc/tycho-extras/serialized-form.html
/usr/share/javadoc/tycho-extras/stylesheet.css

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
