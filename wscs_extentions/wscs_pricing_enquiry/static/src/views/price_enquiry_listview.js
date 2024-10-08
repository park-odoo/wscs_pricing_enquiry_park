/** @odoo-module **/

import { registry } from "@web/core/registry";
import { listView } from "@web/views/list/list_view";
import { ListRenderer } from "@web/views/list/list_renderer";
import { PriceEnquiryDashBoard } from '@wscs_pricing_enquiry/views/price_enquiry_dashboard';

export class PriceEnquiryDashBoardRenderer extends ListRenderer {};

PriceEnquiryDashBoardRenderer.template = 'wscs_pricing_enquiry.PriceEnquiryListView';
PriceEnquiryDashBoardRenderer.components= Object.assign({}, ListRenderer.components, {PriceEnquiryDashBoard})

export const PriceEnquiryDashBoardListView = {
    ...listView,
    Renderer: PriceEnquiryDashBoardRenderer,
};

registry.category("views").add("price_enquiry_dashboard_list", PriceEnquiryDashBoardListView);
