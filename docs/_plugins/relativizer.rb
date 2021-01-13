require 'pathname'

module Jekyll
  module UrlRelativizer
    def relativize_url(url)
      pageUrl = @context.registers[:page]["url"]
      pageDir = Pathname(pageUrl).parent
      Pathname(url).relative_path_from(pageDir).to_s
    end
  end
end

Liquid::Template.register_filter(Jekyll::UrlRelativizer)