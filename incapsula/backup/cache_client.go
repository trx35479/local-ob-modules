package incapsula

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/url"
)

// Endpoints (unexported consts)
const endpointCacheRuleAdd = "sites/performance/caching-rules/add"
const endpointCacheRuleList = "sites/performance/caching-rules/list"
const endpointCacheRuleEdit = "sites/performance/caching-rules/edit"
const endpointCacheRuleDelete = "sites/performance/caching-rules/delete"
const endpointCacheEnableDisable = "sites/performance/caching-rules/enable"

// Cache action rule Actions
const actionHttpCacheStatic = "HTTP_CACHE_MAKE_STATIC"
const actionHttpCacheClient = "HTTP_CACHE_CLIENT_CACHE_CTL"
const actionHttpForceUncacheable = "HTTP_CACHE_FORCE_UNCACHEABLE"
const actionHttpDifferentiateSsl = "HTTP_CACHE_DIFFERENTIATE_SSL"
const actionHttpDifferentiateByHeader = "HTTP_CACHE_DIFFERENTIATE_BY_HEADER"
const actionHttpDifferentiateByCookie = "HTTP_CACHE_DIFFERENTIATE_BY_COOKIE"
const actionHttpIgnoreParams = "HTTP_CACHE_IGNORE_PARAMS"
const actionHttpIgnoreAuthHeader = "HTTP_CACHE_IGNORE_AUTH_HEADER"
const actionHttpForceValidation = "HTTP_CACHE_FORCE_VALIDATION"
const actionHttpAddTag = "HTTP_CACHE_ADD_TAG"
const actionHttpEnrichCacheKey = "HTTP_CACHE_ENRICH_CACHE_KEY"

// Incap cache rul respose struct
type CacheRuleAddResponse struct {
	Res        int    `json:"res"`
	ResMessage string `json:"res_message"`
	RuleID     string `json:"rule_id"`
	DebugInfo  struct {
		IDInfo string `json:"id_info"`
		SiteID string `json:"site_id"`
	} `json:"debug_info"`
}

// Incap cache rule update response
type CacheRuleEditResponse struct {
	Res        string `json:"res"`
	ResMessage string `json:"res_message"`
}

// Incap cache rule list
type CacheRuleListResponse struct{}

// Incap cache rule delete
type CacheRuleDeleteResponse struct {
	Res        string `json:"res"`
	ResMessage string `json:"res_message"`
}

func (c *Client) AddCacheRule(name, siteID, action, filter, ruleID, ttl_unit, differentiatedByValue, params, tagName, text, allParams, ttl string) (*CacheRuleAddResponse, error) {
	log.Printf("[INFO] Adding Incapsula cache rule for siteID: %s\n", siteID)

	// url values
	values := url.Values{
		"api_id":  {c.config.APIID},
		"api_key": {c.config.APIKey},
		"name":    {name},
		"site_id": {siteID},
		"action":  {action},
		//	"filter":  {filter},
	}
	// switch values for different action
	switch action {
	case actionHttpCacheStatic:
		values.Add("ttl", ttl)
		values.Add("ttl_unit", ttl_unit)
	case actionHttpCacheClient:
		values.Add("ttl", ttl)
		values.Add("ttl_unit", ttl_unit)
	case actionHttpForceUncacheable:
		fallthrough
	case actionHttpDifferentiateSsl:
		fallthrough
	case actionHttpDifferentiateByHeader:
		values.Add("filter", filter)
	case actionHttpDifferentiateByCookie:
		fallthrough
	case actionHttpIgnoreParams:
		values.Add("params", params)
		values.Add("all_params", allParams)
	case actionHttpIgnoreAuthHeader:
		fallthrough
	case actionHttpForceValidation:
		fallthrough
	case actionHttpAddTag:
		values.Add("tag_name", tagName)
	case actionHttpEnrichCacheKey:
		values.Add("text", text)
	}

	// Post for Incapsula
	resp, err := c.httpClient.PostForm(fmt.Sprintf("%s/%s", c.config.BaseURL, endpointCacheRuleAdd), values)
	if err != nil {
		return nil, fmt.Errorf("Error from Incapsula service when adding cache rule for siteID %s: %s", siteID, err)
	}

	defer resp.Body.Close()
	responseBody, err := ioutil.ReadAll(resp.Body)

	// Dump JSON
	log.Printf("[DEBUG] Incapsula add cache rule JSON response: %s\n", string(responseBody))

	// Parse the JSON
	var cacheRuleAddResponse CacheRuleAddResponse
	err = json.Unmarshal([]byte(responseBody), &cacheRuleAddResponse)
	if err != nil {
		return nil, fmt.Errorf("Error parsing add cache rule JSON response for siteID %s: %s\nresponse: %s", siteID, err, string(responseBody))
	}

	// Look at the response status code from Incapsula
	if cacheRuleAddResponse.Res != 0 {
		return nil, fmt.Errorf("Error from Incapsula service Res is not equal to 0 when adding cache rule for siteID %s: %s", siteID, string(responseBody))
	}

	return &cacheRuleAddResponse, nil
}

func (c *Client) ListCacheRule(siteID string) (*CacheRuleListResponse, error) {
	log.Printf("[INFO] Listing Incapsula cache rule for siteID: %s\n", siteID)

	resp, err := c.httpClient.PostForm(fmt.Sprintf("%s/%s", c.config.BaseURL, endpointCacheRuleList), url.Values{
		"api_id":  {c.config.APIID},
		"api_key": {c.config.APIKey},
		"site_id": {siteID},
	})

	if err != nil {
		return nil, fmt.Errorf("Error from Incapsula service when listing cache rule for siteID %s: %s", siteID, err)
	}
	// Read the body
	defer resp.Body.Close()
	responseBody, err := ioutil.ReadAll(resp.Body)

	// Dump JSON
	log.Printf("[DEBUG] Incapsula add cache rule JSON response: %s\n", string(responseBody))

	// Parse the JSON
	var cacheRuleListResponse CacheRuleListResponse
	err = json.Unmarshal([]byte(responseBody), &cacheRuleListResponse)
	if err != nil {
		return nil, fmt.Errorf("Error parsing list cache rule JSON response for siteID %s: %s\nresponse: %s", siteID, err, string(responseBody))
	}

	// Look at the response status code from Incapsula
	//	if cacheRuleListResponse.Res != "0" {
	//		return nil, fmt.Errorf("Error from Incapsula service when listing cache rule for siteID %s: %s", siteID, string(responseBody))
	//	}

	return &cacheRuleListResponse, nil
}

func (c *Client) EditCacheRule(name, siteID, ruleID, action, filter, ttl_unit, differentiatedByValue, params, tagName, text, allParams, ttl string) (*CacheRuleEditResponse, error) {
	log.Printf("[INFO] Updating Incapsula cache rule for siteID: %s\n", siteID)

	values := url.Values{
		"api_id":  {c.config.APIID},
		"api_key": {c.config.APIKey},
		"site_id": {siteID},
		"action":  {action},
		"filter":  {filter},
		"name":    {name},
		"rule_id": {ruleID},
	}

	switch action {
	case actionHttpCacheStatic:
		values.Add("ttl", ttl)
		values.Add("ttl_unit", ttl_unit)
	case actionHttpCacheClient:
		values.Add("ttl", ttl)
		values.Add("ttl_unit", ttl_unit)
	case actionHttpForceUncacheable:
		fallthrough
	case actionHttpDifferentiateSsl:
		fallthrough
	case actionHttpDifferentiateByHeader:
		fallthrough
	case actionHttpDifferentiateByCookie:
		fallthrough
	case actionHttpIgnoreParams:
		values.Add("params", params)
		values.Add("all_params", allParams)
	case actionHttpIgnoreAuthHeader:
		fallthrough
	case actionHttpForceValidation:
		fallthrough
	case actionHttpAddTag:
		values.Add("tag_name", tagName)
	case actionHttpEnrichCacheKey:
		values.Add("text", text)
	}

	resp, err := c.httpClient.PostForm(fmt.Sprintf("%s/%s", c.config.BaseURL, endpointCacheRuleEdit), values)

	if err != nil {
		return nil, fmt.Errorf("Error from Incapsula service when listing cache rule for siteID %s: %s", siteID, err)
	}
	// Read the body
	defer resp.Body.Close()
	responseBody, err := ioutil.ReadAll(resp.Body)

	// Dump JSON
	log.Printf("[DEBUG] Incapsula add cache rule JSON response: %s\n", string(responseBody))

	// Parse the JSON
	var cacheRuleEditResponse CacheRuleEditResponse
	err = json.Unmarshal([]byte(responseBody), &cacheRuleEditResponse)
	if err != nil {
		return nil, fmt.Errorf("Error parsing list cache rule JSON response for siteID %s: %s\nresponse: %s", siteID, err, string(responseBody))
	}

	// Look at the response status code from Incapsula
	if cacheRuleEditResponse.Res != "0" {
		return nil, fmt.Errorf("Error from Incapsula service when listing cache rule for siteID %s: %s", siteID, string(responseBody))
	}

	return &cacheRuleEditResponse, nil
}

func (c *Client) DeleteCacheRule(siteID, ruleID string) (*CacheRuleDeleteResponse, error) {
	log.Printf("[INFO] Deleting Incapsula cache rule for siteID: %s\n", siteID)

	resp, err := c.httpClient.PostForm(fmt.Sprintf("%s/%s", c.config.BaseURL, endpointCacheRuleEdit), url.Values{
		"api_id":  {c.config.APIID},
		"api_key": {c.config.APIKey},
		"site_id": {siteID},
		"rule_id": {ruleID},
	})
	if err != nil {
		return nil, fmt.Errorf("Error from Incapsula service when listing cache rule for siteID %s: %s", siteID, err)
	}
	// Read the body
	defer resp.Body.Close()
	responseBody, err := ioutil.ReadAll(resp.Body)

	// Dump JSON
	log.Printf("[DEBUG] Incapsula add cache rule JSON response: %s\n", string(responseBody))

	// Parse the JSON
	var cacheRuleDeleteResponse CacheRuleDeleteResponse
	err = json.Unmarshal([]byte(responseBody), &cacheRuleDeleteResponse)
	if err != nil {
		return nil, fmt.Errorf("Error parsing list cache rule JSON response for siteID %s: %s\nresponse: %s", siteID, err, string(responseBody))
	}

	// Look at the response status code from Incapsula
	if cacheRuleDeleteResponse.Res != "0" {
		return nil, fmt.Errorf("Error from Incapsula service when listing cache rule for siteID %s: %s", siteID, string(responseBody))
	}

	return &cacheRuleDeleteResponse, nil
}
