<?rsa version="1.0" encoding="utf-8"?>
<Configuration>
	<Product Id="Crypto-C ME">
		<Version>CRYPTO-C ME 2.1.0.3</Version>
		<ReleaseDate>""</ReleaseDate>
		<ExpDate>""</ExpDate>
		<Copyright>
			Copyright (C) RSA
		</Copyright>
		<Library Id="master">cryptocme2</Library>
	</Product>
	<Runtime Id="runtime">
		<LoadOrder>
			<Library Id="ccme_base">ccme_base</Library>
			<Library Id="ccme_ecc">ccme_ecc</Library>
			<Library Id="ccme_eccaccel">ccme_eccaccel</Library>
		</LoadOrder>
		<StartupConfig>
			<SelfTest>OnLoad</SelfTest>
		</StartupConfig>
	</Runtime>
	<Signature URI="#ccme_base" Algorithm="FIPS140_INTEGRITY">MC0CFQCym9a3ch9edyt3puH5yIjMLgzx6QIUPjDRlngU4/GfLW9hxQI2YqXGUqw=</Signature>
	<Signature URI="#ccme_ecc" Algorithm="FIPS140_INTEGRITY">MC0CFQDU1MznFncB6jkIUJ0IPjn9DmJKRAIUOL4dG8KiatvgThsIY/GiH2JnCY4=</Signature>
	<Signature URI="#ccme_eccaccel" Algorithm="FIPS140_INTEGRITY">MC0CFQCBOpr4g/Qr6Ze2xkOqFFnUaxyrpgIUCd+pOKVnJyuQnOQ1OE5zgCCOke0=</Signature>
	<Signature URI="#master" Algorithm="FIPS140_INTEGRITY">MCwCFDtnCUkmOzB8hjezWR4UPCBXlwj+AhRwyBHMT50huozatQ2sjZ2SjZ//zQ==</Signature>
	<Signature URI="#Crypto-C ME" Algorithm="FIPS140_INTEGRITY">MC0CFQDhpSNTpTO6T8z/56M3Y+0mG+d42AIUUd8PvCxJTR3R/dzC7UiDwoWi2Ds=</Signature>
	<Signature URI="#runtime" Algorithm="FIPS140_INTEGRITY">MCwCFExCjnscUZYGBCgcGER6jgYl3omFAhQWm/YfQC7pfkTDo1pvwAPocZjxlg==</Signature>
</Configuration>

