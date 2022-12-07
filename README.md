# Model-based Methodology for Secure Development and Testing
Digital transformation is heavily changing the industrial landscape: modern industries widely rely upon advanced ICT technologies and complex software systems to build value-added services and products that very often have a significant impact on our lives. It is widely recognized that, in this context, security is a
mandatory property to ensure, but still many organizations lag behind when it comes to building security into their services. Recently, there is a growing interest in secure development methodologies where security plays a key role throughout the development lifecycle. To fit within the continuous integration and delivery frameworks,
security-related activities are currently supported by tools that enable automated operations such as code analysis, vulnerability scanning, security testing, security monitoring, and security policy verification. Although existing tools can be helpful to handle security throughout the development and operation lifecycle, manual interventions of security experts are still required, not only in those activities that can be hardly automated but also to configure and process the output of the security testing tools.

We propose a novel secure development methodology aimed at supporting security design and testing through semi-automated activities. The proposed methodology leverages a model-based process that enables identifying existing threats, evaluating the associated risks, and verifying the proper enforcement of the mitigation measures expected against the applicable threats through static assessment procedures and targeted security tests. 

## ThreatCatalogue.xlsx
It comprises a collection of threats related to the assets (e.g., database, web server, etc) that typically compose modern software systems. Our Threat Catalogue correlates threats, assets, and [NIST security control](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#/families?version=5.1). Moreover, it also provides an excel sheet that reports useful information concerning MTD techniques and their implementation.

The catalogue is fully extensible, any suggestions or contributions are really welcomed!

## Threat_AttackPattern_Catalogue.xlsx
It provides the association between a collection of threats related to assets and [CAPEC attack patterns](https://capec.mitre.org/), common attributes and approaches used by attackers when exploiting a weakness in computer systems.

## AttackPattern_Attack_Catalogue.xlsx
It binds CAPEC attack patterns and [MITRE ATT&CK](https://attack.mitre.org/), which is a knowledge base of adversary tactics and techniques. 

## Usage
To effectively use the proposed approach, a developer should follow the following steps:

1.  Model an application according to the asset type supported by ThreatCatalogue.xlsx;
2.  Collect all the threats that threaten its application;
3.  Implement corresponding security controls;
4.  Identify attack patterns associated with the retrieved threats;
5.  Identify attack tactics and techniques corresponding to previously retrieved attack patterns;
6.  Test the applications against the collected tactics and techniques;
7.  Successful test force the developer to fix corresponding security controls.
