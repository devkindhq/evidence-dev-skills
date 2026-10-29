# Evidence.dev Skills: Agent Skills for Evidence.dev

Agent Skills for [Evidence.dev](https://docs.evidence.dev), the SQL-first analytics framework. Nine skills that teach AI coding agents (Claude Code, skills.sh-compatible agents, any agent that reads SKILL.md files) to build Evidence pages, charts, inputs, maps and data sources correctly.

Built by [Devkind](https://devkind.com.au). Maintained by Kazim Ali. Follows the [Agent Skills](https://agentskills.io) convention: every skill is a `skills/<name>/SKILL.md` with `name` + `description` frontmatter, so it drops straight into Claude Code, skills.sh, or your own agent runtime.

## What you get

Nine focused skills covering the full Evidence.dev surface, from writing your first SQL-in-markdown page to deploying it:

| # | Skill | Covers |
|---|-------|--------|
| 1 | `evidence-core-concepts` | SQL queries in markdown, templated pages, loops, if/else, formatting, query functions, exports, themes |
| 2 | `evidence-charts` | LineChart, BarChart, AreaChart, ScatterPlot, BubbleChart, Histogram, FunnelChart, Heatmap, CalendarHeatmap, BoxPlot, Sparkline, SankeyDiagram, custom ECharts |
| 3 | `evidence-data-components` | BigValue, DataTable, Delta, Value |
| 4 | `evidence-inputs` | Dropdown, TextInput, Checkbox, DateInput, DateRange, Slider, ButtonGroup, DimensionGrid + query integration |
| 5 | `evidence-maps` | AreaMap, BaseMap, BubbleMap, PointMap, USMap |
| 6 | `evidence-ui` | Accordion, Alert, Grid, Tabs, Modal, Note, Details, DownloadData, Embed, Link, PrintFormat and more |
| 7 | `evidence-data-sources` | BigQuery, PostgreSQL, MySQL, DuckDB, Snowflake, CSV, SQLite, Motherduck, Databricks, Redshift, Trino, Google Sheets, JavaScript sources |
| 8 | `evidence-cli` | Dev server, build, rendering modes, environment variables, deployment |
| 9 | `evidence-custom` | Custom Svelte components, component queries, plugin development and publishing |

## Install

**Any agent (skills.sh):**

```bash
npx skills add devkindhq/evidence-dev-skills
```

**Claude Code (plugin marketplace):**

```
/plugin marketplace add devkindhq/evidence-dev-skills
/plugin install evidence-dev-skills@evidence-dev-skills
```

Or clone the repo and copy whichever `skills/<name>` folders you need into your agent's skills directory.

## Example usage

Once installed, just ask your agent in plain language. The skill descriptions trigger automatically:

> Build an Evidence page with a date range filter, a BigValue showing total revenue and a BarChart of revenue by category.

Your agent will pull in `evidence-inputs`, `evidence-data-components` and `evidence-charts` and write:

````mdx
<DateRange name="dates" defaults={[dateMod('90 days ago'), dateMod('today')]} />

```sql revenue_by_category
select category, sum(amount) as revenue
from orders
where order_date between '${inputs.dates.start}' and '${inputs.dates.end}'
group by 1
```

<BigValue value={revenue_by_category} column=revenue summarise=total />
<BarChart data={revenue_by_category} x=category y=revenue />
````

Switching to DuckDB or Snowflake? Ask about data sources and `evidence-data-sources` guides the `connection.yaml` setup. Deploying? `evidence-cli` covers build modes and platform config.

## License

[MIT](LICENSE) © Devkind. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
