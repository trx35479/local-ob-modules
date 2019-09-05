package incapsula

import (
	"fmt"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"
)

////////////////////////////////////////////////////////////////
// ConfigureACLSecurityRule Tests
////////////////////////////////////////////////////////////////

func TestClientConfigureWAFSecurityRuleBadConnection(t *testing.T) {
	config := &Config{APIID: "foo", APIKey: "bar", BaseURL: "badness.incapsula.com"}
	client := &Client{config: config, httpClient: &http.Client{Timeout: time.Millisecond * 1}}
	siteID, ruleID := 42, "42"
	configureWAFSecurityRuleResponse, err := client.ConfigureWafSecurity(siteID, ruleID, "", "", "", "", "", "")
	if err == nil {
		t.Errorf("Should have received an error")
	}
	if !strings.HasPrefix(err.Error(), fmt.Sprintf("Error adding WAF Security for rule id %s and site id %d", ruleID, siteID)) {
		t.Errorf("Should have received an client error, got: %s", err)
	}
	if configureWAFSecurityRuleResponse != nil {
		t.Errorf("Should have received a nil configureWAFSecurityRuleResponse instance")
	}
}

func TestClientConfigureWAFSecurityRuleBadJSON(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(rw http.ResponseWriter, req *http.Request) {
		if req.URL.String() != fmt.Sprintf("/%s", endpointWafSecurityConfigure) {
			t.Errorf("Should have have hit /%s endpoint. Got: %s", endpointWafSecurityConfigure, req.URL.String())
		}
		rw.Write([]byte(`{`))
	}))
	defer server.Close()

	config := &Config{APIID: "foo", APIKey: "bar", BaseURL: server.URL}
	client := &Client{config: config, httpClient: &http.Client{}}
	siteID, ruleID := 42, "42"
	configureWAFSecurityRuleResponse, err := client.ConfigureWafSecurity(siteID, ruleID, "", "", "", "", "", "")
	if err == nil {
		t.Errorf("Should have received an error")
	}
	if !strings.HasPrefix(err.Error(), fmt.Sprintf("Error parsing add WAF rule JSON response for rule id %s and site id %d", ruleID, siteID)) {
		t.Errorf("Should have received a JSON parse error, got: %s", err)
	}
	if configureWAFSecurityRuleResponse != nil {
		t.Errorf("Should have received a nil configureWAFSecurityRuleResponse instance")
	}
}

func TestClientConfigureWAFSecurityRuleInvalidSite(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(rw http.ResponseWriter, req *http.Request) {
		if req.URL.String() != fmt.Sprintf("/%s", endpointWafSecurityConfigure) {
			t.Errorf("Should have have hit /%s endpoint. Got: %s", endpointWafSecurityConfigure, req.URL.String())
		}
		rw.Write([]byte(`{"site_id":0,"res":1}`))
	}))
	defer server.Close()

	config := &Config{APIID: "foo", APIKey: "bar", BaseURL: server.URL}
	client := &Client{config: config, httpClient: &http.Client{}}
	siteID, ruleID := 42, "42"
	configureWAFSecurityRuleResponse, err := client.ConfigureWafSecurity(siteID, ruleID, "", "", "", "", "", "")
	if err == nil {
		t.Errorf("Should have received an error")
	}
	if !strings.HasPrefix(err.Error(), fmt.Sprintf("Error from Incapsula service when adding WAF rule for rule id %s and site id %d: %s", ruleID, siteID, string(`{"site_id":0,"res":1}`))) {
		t.Errorf("Should have received a bad site error, got: %s", err)
	}
	if configureWAFSecurityRuleResponse != nil {
		t.Errorf("Should have received a nil configureWAFSecurityRuleResponse instance")
	}
}

func TestClientConfigureWAFSecurityRuleValidSite(t *testing.T) {
	server := httptest.NewServer(http.HandlerFunc(func(rw http.ResponseWriter, req *http.Request) {
		if req.URL.String() != fmt.Sprintf("/%s", endpointWafSecurityConfigure) {
			t.Errorf("Should have have hit /%s endpoint. Got: %s", endpointWafSecurityConfigure, req.URL.String())
		}
		rw.Write([]byte(`{"site_id":123,"res":0}`))
	}))
	defer server.Close()

	config := &Config{APIID: "foo", APIKey: "bar", BaseURL: server.URL}
	client := &Client{config: config, httpClient: &http.Client{}}
	siteID, ruleID := 42, "42"
	configureWAFSecurityRuleResponse, err := client.ConfigureWafSecurity(siteID, ruleID, "", "", "", "", "", "")
	if err != nil {
		t.Errorf("Should not have received an error")
	}
	if configureWAFSecurityRuleResponse == nil {
		t.Errorf("Should not have received a nil configureWAFSecurityRuleResponse instance")
	}
	if configureWAFSecurityRuleResponse.SiteID != 123 {
		t.Errorf("Site ID doesn't match")
	}
	if configureWAFSecurityRuleResponse.Res != 0 {
		t.Errorf("Response code doesn't match")
	}
}
