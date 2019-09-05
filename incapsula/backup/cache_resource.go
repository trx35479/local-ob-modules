package incapsula

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/hashicorp/terraform/helper/schema"
)

func resourceCacheRule() *schema.Resource {
	return &schema.Resource{
		Create: resourceCacheRuleAdd,
		Read:   resourceCacheRuleList,
		Update: resourceCacheRuleEdit,
		Delete: resourceCacheRuleDelete,
		Importer: &schema.ResourceImporter{
			State: func(d *schema.ResourceData, meta interface{}) ([]*schema.ResourceData, error) {
				idSlice := strings.Split(d.Id(), "/")
				if len(idSlice) != 2 || idSlice[0] == "" || idSlice[1] == "" {
					return nil, fmt.Errorf("unexpected format of ID (%q), expected site_id/rule_id", d.Id())
				}

				siteID, err := strconv.Atoi(idSlice[0])
				//ruleID := idSlice[1]
				if err != nil {
					return nil, err
				}

				d.Set("site_id", siteID)
				return []*schema.ResourceData{d}, nil
			},
		},

		Schema: map[string]*schema.Schema{
			// Required attributes
			"site_id": {
				Description: "Numeric identifier of the site to operate on.",
				Type:        schema.TypeString,
				Required:    true,
				ForceNew:    true,
			},
			"name": {
				Description: "Rule name.",
				Type:        schema.TypeString,
				Required:    true,
				ForceNew:    true,
			},
			"action": {
				Description: "Rule action.",
				Type:        schema.TypeString,
				Required:    true,
			},
			// optional attributes
			"filter": {
				Description: "Rule will trigger only a request that matches this filter. For more details on filters, see Syntax Guide.",
				Type:        schema.TypeString,
				Optional:    true,
			},
			"ttl": {
				Description: "Rule TTL. Only relevant when action is HTTP_CACHE_MAKE_STATIC or HTTP_CACHE_CLIENT_CACHE_CTL.",
				Type:        schema.TypeString,
				Optional:    true,
			},
			"ttl_unit": {
				Description: "Must be one of SECONDS, MINUTES, HOURS, DAYS or WEEKS. If no time unit is provided, SECONDS is used.",
				Type:        schema.TypeString,
				Optional:    true,
			},
			"differentiated_by_value": {
				Description: "Value to differentiate by.",
				Type:        schema.TypeString,
				Optional:    true,
			},
			"params": {
				Description: "Comma separated list of parameters to ignore.",
				Type:        schema.TypeString,
				Optional:    true,
			},
			"all_params": {
				Description: "When set to true: all parameters in cache key will be ignored.",
				Type:        schema.TypeString,
				Optional:    true,
			},
			"tag_name": {
				Description: "The name of the tag to add.",
				Type:        schema.TypeString,
				Optional:    true,
			},
			"text": {
				Description: "Add text to the cache key as suffix. Relevant for the HTTP_CACHE_ENRICH_CACHE_KEY action",
				Type:        schema.TypeString,
				Optional:    true,
			},
		},
	}
}

func resourceCacheRuleAdd(d *schema.ResourceData, m interface{}) error {
	client := m.(*Client)

	addCacheRuleResponse, err := client.AddCacheRule(
		getStringValue(d.Get("name")),
		getStringValue(d.Get("action")),
		getStringValue(d.Get("site_id")),
		getStringValue(d.Get("filter")),
		getStringValue(d.Id()),
		getStringValue(d.Get("ttl")),
		getStringValue(d.Get("ttl_unit")),
		getStringValue(d.Get("differentiated_by_value")),
		getStringValue(d.Get("params")),
		getStringValue(d.Get("all_params")),
		getStringValue(d.Get("tag_name")),
		getStringValue(d.Get("text")),
	)

	if err != nil {
		return err
	}

	d.SetId(addCacheRuleResponse.RuleID)

	return resourceCacheRuleList(d, m)
}

func resourceCacheRuleList(d *schema.ResourceData, m interface{}) error {
	client := m.(*Client)

	//listCacheRuleResponse,
	_, err := client.ListCacheRule(getStringValue(d.Get("site_id")))
	if err != nil {
		return err
	}

	//for _, cacheRule := range listCacheRuleResponse.Actions {
	//	if cacheRule.action == d.Get("action").(string) {
	//		d.Set(listCacheRuleResponse.action)
	//		d.Set(listCacheRuleResponse.Id)
	//	}
	//}

	return nil
}

func resourceCacheRuleEdit(d *schema.ResourceData, m interface{}) error {
	client := m.(*Client)

	_, err := client.EditCacheRule(
		getStringValue(d.Id()),
		getStringValue(d.Get("name")),
		getStringValue(d.Get("action")),
		getStringValue(d.Get("site_id")),
		getStringValue(d.Get("filter")),
		getStringValue(d.Get("ttl")),
		getStringValue(d.Get("ttl_unit")),
		getStringValue(d.Get("differentiated_by_value")),
		getStringValue(d.Get("params")),
		getStringValue(d.Get("all_params")),
		getStringValue(d.Get("tag_name")),
		getStringValue(d.Get("text")),
	)

	if err != nil {
		return err
	}

	return nil
}

func resourceCacheRuleDelete(d *schema.ResourceData, m interface{}) error {
	client := m.(*Client)

	_, err := client.DeleteCacheRule(getStringValue(d.Get("site_id")), d.Id())

	if err != nil {
		return nil
	}
	// clear the id
	d.SetId("")

	return nil
}
