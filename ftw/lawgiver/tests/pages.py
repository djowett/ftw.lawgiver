from ftw.testing import browser
from ftw.testing.pages import Plone
from operator import attrgetter


class SpecItem(object):

    def __init__(self, dtnode, ddnode):
        self.dtnode = dtnode
        self.ddnode = ddnode

    def link_text(self):
        return self.dtnode.find_by_xpath('a').text

    def link_href(self):
        return self.dtnode.find_by_xpath('a').first['href']

    def description(self):
        return self.ddnode.text

    def click(self):
        browser().find_link_by_text(self.link_text()).click()

    def __repr__(self):
        return '<SpecItem "%s">' % self.link_text()


class SpecsListing(Plone):

    def open(self):
        browser().visit(self.listing_url)
        assert self.get_template_class() == 'template-lawgiver-list-specs', \
            'Not on @@lawgiver-list-specs view!?: %s' % browser().url

    @property
    def listing_url(self):
        return '/'.join((self.portal_url, '@@lawgiver-list-specs'))

    def get_specifications(self):
        result = []

        for dtnode in browser().find_by_xpath(
            '//dl[@class="specifications"]/dt'):

            ddnode = dtnode.find_by_xpath('following-sibling::*[self::dd]')
            result.append(SpecItem(dtnode, ddnode))

        return result

    def get_specification_by_text(self, text):
        for spec in self.get_specifications():
            if spec.link_text() == text:
                return spec

        raise KeyError('Specification link with text "%s" not found' % text)


class SpecDetails(Plone):

    def get_spec_metadata_table(self):
        data = []

        for row in browser().find_by_css('table.spec-metadata tr'):
            th = row.find_by_xpath('th').first
            td = row.find_by_xpath('td').first
            data.append((th.text, td.text))

        return data

    def get_specification_text(self):
        return browser().find_by_css('dl.specification dd pre').first.text

    def get_specification_mapping(self):
        mapping = {}

        groups = browser().find_by_css('dl.permission-mapping dd dl dt')
        for actiongroup in groups:
            groupname = actiongroup.text

            permissionlist = actiongroup.find_by_xpath(
                'following-sibling::*[self::dd]').first

            permissions = map(attrgetter('text'),
                              permissionlist.find_by_css('li'))
            mapping[groupname] = permissions

        return mapping

    def get_unmanaged_permissions(self):
        return map(attrgetter('text'),
                   browser().find_by_css('dl.unmanaged-permissions dd li'))

    def button_write(self):
        return self.get_button('Write workflow definition')

    def button_write_and_import(self):
        return self.get_button('Write and Import Workflow')

    def button_reindex(self):
        return self.get_button('Update security settings')