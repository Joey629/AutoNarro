---
id: Tabs
section: components
cssPrefix: pf-v6-c-tabs
---# Examples

## Default

### Default tabs example

```html
<div
  class="pf-v6-c-tabs"
  aria-label="Default example"
  role="region"
  id="default-tabs"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul class="pf-v6-c-tabs__list" role="tablist" aria-label="Default example">
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="default-tabs-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="default-tabs-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="default-tabs-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Default tabs usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-m-disabled` | `a.pf-v6-c-tabs__link` | Modifies a tabs link for disabled styles. |
| `.pf-m-aria-disabled` | `.pf-v6-c-tabs__link` | Modifies a tabs link for disabled styles, but is still hoverable/focusable. |

## Overflow

### Overflow beginning of list example

```html
<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Overflow beginning of list example"
  role="region"
  id="overflow-beginning-of-list"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Overflow beginning of list example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="overflow-beginning-of-list-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="overflow-beginning-of-list-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="overflow-beginning-of-list-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="overflow-beginning-of-list-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="overflow-beginning-of-list-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="overflow-beginning-of-list-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="overflow-beginning-of-list-cloud-link"
      >
        <span class="pf-v6-c-tabs__item-text">Hybrid Cloud</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="overflow-beginning-of-list-automation-link"
      >
        <span class="pf-v6-c-tabs__item-text">Automation</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="overflow-beginning-of-list-files-link"
      >
        <span class="pf-v6-c-tabs__item-text">Files</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Overflow beginning of list usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-m-scrollable` | `.pf-v6-c-tabs` | Enables the directional scroll buttons. |
| `.pf-v6-c-tabs__scroll-button` | `<div>` | Initiates a tabs component scroll button container. |

### Horizontal overflow example

```html
<div
  class="pf-v6-c-tabs pf-m-overflow"
  aria-label="Horizontal overflow example"
  role="region"
  id="horizontal-overflow"
>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Horizontal overflow example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="horizontal-overflow-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-overflow" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-more-link"
      >
        <span class="pf-v6-c-tabs__item-text">More</span>
        <span class="pf-v6-c-tabs__link-toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
            />
          </svg>
        </span>
      </button>
    </li>
  </ul>
</div>

```

### Horizontal overflow expanded example

```html
<div
  class="pf-v6-c-tabs pf-m-overflow"
  aria-label="Horizontal overflow expanded example"
  role="region"
  id="horizontal-overflow-expanded"
>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Horizontal overflow expanded example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-expanded-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="horizontal-overflow-expanded-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-expanded-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-expanded-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-expanded-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-expanded-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-overflow" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-expanded"
        aria-expanded="true"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-expanded-more-link"
      >
        <span class="pf-v6-c-tabs__item-text">More</span>
        <span class="pf-v6-c-tabs__link-toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
            />
          </svg>
        </span>
      </button>
    </li>
  </ul>
</div>

```

### Horizontal overflow selected example

```html
<div
  class="pf-v6-c-tabs pf-m-overflow"
  aria-label="Horizontal overflow selected example"
  role="region"
  id="horizontal-overflow-selected"
>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Horizontal overflow selected example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-selected-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-selected-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-selected-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-selected-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-selected-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="horizontal-overflow-selected-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-current pf-m-overflow"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="horizontal-overflow-selected-more-link"
      >
        <span class="pf-v6-c-tabs__item-text">More</span>
        <span class="pf-v6-c-tabs__link-toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
            />
          </svg>
        </span>
      </button>
    </li>
  </ul>
</div>

```

## Vertical

### Vertical tabs example

```html
<div
  class="pf-v6-c-tabs pf-m-vertical"
  aria-label="Vertical tabs example"
  role="region"
  id="vertical-tabs"
>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Vertical tabs example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-tabs-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="vertical-tabs-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-tabs-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="vertical-tabs-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="vertical-tabs-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-tabs-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
</div>

```

### Vertical expandable example

```html
<div
  class="pf-v6-c-tabs pf-m-vertical pf-m-expandable"
  aria-label="Vertical expandable example"
  role="region"
  id="vertical-expandable"
>
  <div class="pf-v6-c-tabs__toggle">
    <div class="pf-v6-c-tabs__toggle-button">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-expanded="false"
        aria-label="Details"
        id="vertical-expandable-toggle-button"
        aria-labelledby="vertical-expandable-toggle-text vertical-expandable-toggle-button"
      >
        <span class="pf-v6-c-button__icon pf-m-start">
          <span class="pf-v6-c-tabs__toggle-icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 20 20"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
              />
            </svg>
          </span>
        </span>
        <span class="pf-v6-c-button__text">
          <span
            class="pf-v6-c-tabs__toggle-text"
            id="vertical-expandable-toggle-text"
          >Containers</span>
        </span>
      </button>
    </div>
  </div>

  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Vertical expandable example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="vertical-expandable-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
</div>

```

### Vertical expanded example

```html
<div
  class="pf-v6-c-tabs pf-m-vertical pf-m-expandable pf-m-expanded"
  aria-label="Vertical expanded example"
  role="region"
  id="vertical-expanded"
>
  <div class="pf-v6-c-tabs__toggle">
    <div class="pf-v6-c-tabs__toggle-button">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-expanded="true"
        aria-label="Details"
        id="vertical-expanded-toggle-button"
        aria-labelledby="vertical-expanded-toggle-text vertical-expanded-toggle-button"
      >
        <span class="pf-v6-c-button__icon pf-m-start">
          <span class="pf-v6-c-tabs__toggle-icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 20 20"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
              />
            </svg>
          </span>
        </span>
        <span class="pf-v6-c-button__text">
          <span
            class="pf-v6-c-tabs__toggle-text"
            id="vertical-expanded-toggle-text"
          >Containers</span>
        </span>
      </button>
    </div>
  </div>

  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Vertical expanded example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expanded-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="vertical-expanded-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expanded-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expanded-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expanded-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expanded-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
</div>

```

### Vertical expandable responsive example

```html
<div
  class="pf-v6-c-tabs pf-m-vertical pf-m-expandable pf-m-non-expandable-on-md pf-m-expandable-on-lg pf-m-non-expandable-on-xl"
  aria-label="Vertical expandable responsive example"
  role="region"
  id="vertical-expandable-responsive"
>
  <div class="pf-v6-c-tabs__toggle">
    <div class="pf-v6-c-tabs__toggle-button">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-expanded="false"
        aria-label="Details"
        id="vertical-expandable-responsive-toggle-button"
        aria-labelledby="vertical-expandable-responsive-toggle-text vertical-expandable-responsive-toggle-button"
      >
        <span class="pf-v6-c-button__icon pf-m-start">
          <span class="pf-v6-c-tabs__toggle-icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 20 20"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
              />
            </svg>
          </span>
        </span>
        <span class="pf-v6-c-button__text">
          <span
            class="pf-v6-c-tabs__toggle-text"
            id="vertical-expandable-responsive-toggle-text"
          >Containers</span>
        </span>
      </button>
    </div>
  </div>

  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Vertical expandable responsive example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-responsive-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="vertical-expandable-responsive-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-responsive-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-responsive-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-responsive-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-responsive-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
</div>

```

### Vertical expandable example (deprecated)

```html isDeprecated
<div
  class="pf-v6-c-tabs pf-m-vertical pf-m-expandable"
  aria-label="Vertical expandable deprecated example"
  role="region"
  id="vertical-expandable-legacy"
>
  <div class="pf-v6-c-tabs__toggle">
    <div class="pf-v6-c-tabs__toggle-button">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-expanded="false"
        aria-label="Details"
        id="vertical-expandable-legacy-toggle-button"
        aria-labelledby="vertical-expandable-legacy-toggle-text vertical-expandable-legacy-toggle-button"
      >
        <span class="pf-v6-c-button__icon">
          <span class="pf-v6-c-tabs__toggle-icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 20 20"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
              />
            </svg>
          </span>
        </span>
      </button>
    </div>
    <span
      class="pf-v6-c-tabs__toggle-text"
      id="vertical-expandable-legacy-toggle-text"
    >Containers</span>
  </div>

  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Vertical expandable deprecated example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-legacy-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="vertical-expandable-legacy-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-legacy-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-legacy-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-legacy-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-legacy-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
</div>

```

### Vertical expanded example (deprecated)

```html isDeprecated
<div
  class="pf-v6-c-tabs pf-m-vertical pf-m-expandable pf-m-expanded"
  aria-label="Vertical expanded deprecated example"
  role="region"
  id="vertical-expanded-legacy"
>
  <div class="pf-v6-c-tabs__toggle">
    <div class="pf-v6-c-tabs__toggle-button">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-expanded="true"
        aria-label="Details"
        id="vertical-expanded-legacy-toggle-button"
        aria-labelledby="vertical-expanded-legacy-toggle-text vertical-expanded-legacy-toggle-button"
      >
        <span class="pf-v6-c-button__icon">
          <span class="pf-v6-c-tabs__toggle-icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 20 20"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
              />
            </svg>
          </span>
        </span>
      </button>
    </div>
    <span
      class="pf-v6-c-tabs__toggle-text"
      id="vertical-expanded-legacy-toggle-text"
    >Containers</span>
  </div>

  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Vertical expanded deprecated example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expanded-legacy-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="vertical-expanded-legacy-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expanded-legacy-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expanded-legacy-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expanded-legacy-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expanded-legacy-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
</div>

```

### Vertical expandable responsive example (deprecated)

```html isDeprecated
<div
  class="pf-v6-c-tabs pf-m-vertical pf-m-expandable pf-m-non-expandable-on-md pf-m-expandable-on-lg pf-m-non-expandable-on-xl"
  aria-label="Vertical expandable responsive deprecated example"
  role="region"
  id="vertical-expandable-responsive-legacy"
>
  <div class="pf-v6-c-tabs__toggle">
    <div class="pf-v6-c-tabs__toggle-button">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-expanded="false"
        aria-label="Details"
        id="vertical-expandable-responsive-legacy-toggle-button"
        aria-labelledby="vertical-expandable-responsive-legacy-toggle-text vertical-expandable-responsive-legacy-toggle-button"
      >
        <span class="pf-v6-c-button__icon">
          <span class="pf-v6-c-tabs__toggle-icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 20 20"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
              />
            </svg>
          </span>
        </span>
      </button>
    </div>
    <span
      class="pf-v6-c-tabs__toggle-text"
      id="vertical-expandable-responsive-legacy-toggle-text"
    >Containers</span>
  </div>

  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Vertical expandable responsive deprecated example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-responsive-legacy-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="vertical-expandable-responsive-legacy-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-responsive-legacy-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-responsive-legacy-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-responsive-legacy-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="vertical-expandable-responsive-legacy-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
</div>

```

## Box

### Box tabs example

```html
<div
  class="pf-v6-c-tabs pf-m-box"
  aria-label="Box example"
  role="region"
  id="box-tabs"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul class="pf-v6-c-tabs__list" role="tablist" aria-label="Box example">
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="box-tabs-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="box-tabs-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="box-tabs-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Box overflow example

```html
<div
  class="pf-v6-c-tabs pf-m-box pf-m-scrollable"
  aria-label="Box overflow example"
  role="region"
  id="box-overflow"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Box overflow example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-overflow-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="box-overflow-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-overflow-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-overflow-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-overflow-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-overflow-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-overflow-cloud-link"
      >
        <span class="pf-v6-c-tabs__item-text">Hybrid Cloud</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-overflow-automation-link"
      >
        <span class="pf-v6-c-tabs__item-text">Automation</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-overflow-files-link"
      >
        <span class="pf-v6-c-tabs__item-text">Files</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Box vertical example

```html
<div
  class="pf-v6-c-tabs pf-m-vertical pf-m-box"
  aria-label="Box vertical example"
  role="region"
  id="box-vertical"
>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Box vertical example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-vertical-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="box-vertical-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-vertical-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="box-vertical-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="box-vertical-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-vertical-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
</div>

```

### Box tabs secondary variant example

```html
<div
  class="pf-v6-c-tabs pf-m-box pf-m-secondary"
  aria-label="Box secondary variant example"
  role="region"
  id="box-tabs-secondary"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Box secondary variant example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-secondary-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="box-tabs-secondary-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-secondary-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="box-tabs-secondary-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="box-tabs-secondary-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-secondary-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>
<div class="tabs-example-block tabs-example-block--m-secondary"></div>

```

## Tab insets

### Default tab insets example

```html
<div
  class="pf-v6-c-tabs pf-m-inset-sm-on-md pf-m-inset-lg-on-lg pf-m-inset-2xl-on-xl"
  aria-label="Default tab insets example"
  role="region"
  id="default-tab-insets"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Default tab insets example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tab-insets-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="default-tab-insets-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tab-insets-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tab-insets-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tab-insets-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tab-insets-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Box tab insets example

```html
<div
  class="pf-v6-c-tabs pf-m-box pf-m-inset-sm-on-md pf-m-inset-lg-on-lg pf-m-inset-2xl-on-xl"
  aria-label="Box tab insets example"
  role="region"
  id="box-tab-insets"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Box tab insets example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tab-insets-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="box-tab-insets-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tab-insets-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tab-insets-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tab-insets-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tab-insets-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Page insets example

```html
<div
  class="pf-v6-c-tabs pf-m-page-insets"
  aria-label="Page insets example"
  role="region"
  id="page-insets"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Page insets example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="page-insets-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="page-insets-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="page-insets-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="page-insets-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="page-insets-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="page-insets-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Insets usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-m-inset-{none, sm, md, lg, xl, 2xl, 3xl}{-on-[sm, md, lg, xl, 2xl]}` | `.pf-v6-c-tabs` | Modifies the tabs component padding/inset to visually match padding of other adjacent components. |
| `.pf-m-page-insets` | `.pf-v6-c-tabs` | Modifies the tabs component padding/inset to visually match padding of page elements. |

## Icons

### Icons and text example

```html
<div
  class="pf-v6-c-tabs"
  aria-label="Icons and text example"
  role="region"
  id="icons-and-text"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Icons and text example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="icons-and-text-users-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M13.766 21.75H2c-.402 0-.748-.317-.75-.718-.013-3.743 2.34-6.941 5.642-8.201A5.747 5.747 0 0 1 4.25 8a5.76 5.76 0 0 1 6.992-5.619c2.167.456 3.918 2.207 4.376 4.373a5.754 5.754 0 0 1-2.51 6.077c.394.15.77.334 1.134.539.103.058.148.18.113.292a7.924 7.924 0 0 0 .807 6.473.237.237 0 0 1-.054.312c-.485.394-.929.835-1.342 1.303Zm11.342-.919A5.747 5.747 0 0 0 27.75 16c0-3.171-2.58-5.75-5.75-5.75s-5.75 2.579-5.75 5.75a5.747 5.747 0 0 0 2.642 4.831c-3.293 1.257-5.642 4.44-5.642 8.169 0 .414.336.75.75.75h16a.75.75 0 0 0 .75-.75c0-3.73-2.349-6.912-5.642-8.169Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="icons-and-text-containers-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29 9.072v13.855c0 .357-.19.688-.5.866l-12 6.929a1 1 0 0 1-1 0l-12-6.929a1 1 0 0 1-.5-.866V9.072c0-.357.19-.688.5-.866l12-6.929a1.003 1.003 0 0 1 1 0l12 6.929a1 1 0 0 1 .5.866Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="icons-and-text-database-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M3.071 8.5C3.071 4.977 8.991 2 16 2s12.929 2.977 12.929 6.5S23.009 15 16 15 3.071 12.023 3.071 8.5Zm0 4.312V16c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 15.336 21.589 17 16 17S5.632 15.336 3.071 12.812Zm0 7.5V23.5c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 22.835 21.589 24.5 16 24.5S5.632 22.836 3.071 20.312Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="icons-and-text-server-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29.5 9h-27C1.673 9 1 9.673 1 10.5v11c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-11c0-.827-.673-1.5-1.5-1.5ZM13 17.125H8a1.125 1.125 0 0 1 0-2.25h5a1.125 1.125 0 0 1 0 2.25Zm10.005.766a1.874 1.874 0 1 1-.001-3.749 1.874 1.874 0 0 1 .001 3.749Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="icons-and-text-system-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31 27a1 1 0 0 1-1 1H2a1 1 0 1 1 0-2h28a1 1 0 0 1 1 1ZM3 21.5v-16C3 4.673 3.673 4 4.5 4h23c.827 0 1.5.673 1.5 1.5v16c0 .827-.673 1.5-1.5 1.5h-23c-.827 0-1.5-.673-1.5-1.5ZM14.25 8a1.75 1.75 0 1 0 3.5 0 1.75 1.75 0 0 0-3.5 0Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="icons-and-text-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M30 3.5v3c0 .827-.673 1.5-1.5 1.5h-25C2.673 8 2 7.327 2 6.5v-3C2 2.673 2.673 2 3.5 2h25c.827 0 1.5.673 1.5 1.5ZM8.75 22.25h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1Zm10 0h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1Zm10 0h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1ZM16 10a1 1 0 0 0-1 1v3H6.5c-.827 0-1.5.673-1.5 1.5V19a1 1 0 1 0 2 0v-3h8v3a1 1 0 1 0 2 0v-3h8v3a1 1 0 1 0 2 0v-3.5c0-.827-.673-1.5-1.5-1.5H17v-3a1 1 0 0 0-1-1Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

## Sub tabs

### Tabs with sub tabs example

```html
<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="With sub tabs example, primary"
  role="region"
  id="tabs-with-sub-tabs"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="With sub tabs example, primary"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="tabs-with-sub-tabs-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="tabs-with-sub-tabs-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="tabs-with-sub-tabs-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="tabs-with-sub-tabs-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="tabs-with-sub-tabs-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="tabs-with-sub-tabs-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<div
  class="pf-v6-c-tabs pf-m-subtab pf-m-scrollable"
  aria-label="With sub tabs example, Containers"
  role="region"
  id="tabs-with-sub-tabs-subtab"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="With sub tabs example, Containers"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="tabs-with-sub-tabs-subtab-sub-1-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 1</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="tabs-with-sub-tabs-subtab-sub-2-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 2</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="tabs-with-sub-tabs-subtab-sub-3-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 3</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="tabs-with-sub-tabs-subtab-sub-4-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 4</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="tabs-with-sub-tabs-subtab-sub-5-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 5</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="tabs-with-sub-tabs-subtab-sub-6-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 6</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Box tabs with sub tabs example

```html
<div
  class="pf-v6-c-tabs pf-m-box pf-m-scrollable"
  aria-label="Box with sub tabs example, primary"
  role="region"
  id="box-tabs-with-sub-tabs"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Box with sub tabs example, primary"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-with-sub-tabs-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="box-tabs-with-sub-tabs-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-with-sub-tabs-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-with-sub-tabs-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-with-sub-tabs-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-with-sub-tabs-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<div
  class="pf-v6-c-tabs pf-m-subtab pf-m-scrollable"
  aria-label="Box with sub tabs example, Containers"
  role="region"
  id="box-tabs-with-sub-tabs-subtab"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Box with sub tabs example, Containers"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-with-sub-tabs-subtab-sub-1-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 1</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-with-sub-tabs-subtab-sub-2-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 2</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="box-tabs-with-sub-tabs-subtab-sub-3-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 3</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-with-sub-tabs-subtab-sub-4-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 4</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-with-sub-tabs-subtab-sub-5-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 5</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-with-sub-tabs-subtab-sub-6-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 6</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

## Filled

### Filled tabs example

```html
<div
  class="pf-v6-c-tabs pf-m-fill"
  aria-label="Filled example"
  role="region"
  id="filled-tabs"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul class="pf-v6-c-tabs__list" role="tablist" aria-label="Filled example">
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="filled-tabs-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="filled-tabs-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="filled-tabs-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Filled with icons example

```html
<div
  class="pf-v6-c-tabs pf-m-fill"
  aria-label="Filled with icons example"
  role="region"
  id="filled-with-icons"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Filled with icons example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="filled-with-icons-users-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M13.766 21.75H2c-.402 0-.748-.317-.75-.718-.013-3.743 2.34-6.941 5.642-8.201A5.747 5.747 0 0 1 4.25 8a5.76 5.76 0 0 1 6.992-5.619c2.167.456 3.918 2.207 4.376 4.373a5.754 5.754 0 0 1-2.51 6.077c.394.15.77.334 1.134.539.103.058.148.18.113.292a7.924 7.924 0 0 0 .807 6.473.237.237 0 0 1-.054.312c-.485.394-.929.835-1.342 1.303Zm11.342-.919A5.747 5.747 0 0 0 27.75 16c0-3.171-2.58-5.75-5.75-5.75s-5.75 2.579-5.75 5.75a5.747 5.747 0 0 0 2.642 4.831c-3.293 1.257-5.642 4.44-5.642 8.169 0 .414.336.75.75.75h16a.75.75 0 0 0 .75-.75c0-3.73-2.349-6.912-5.642-8.169Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="filled-with-icons-containers-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29 9.072v13.855c0 .357-.19.688-.5.866l-12 6.929a1 1 0 0 1-1 0l-12-6.929a1 1 0 0 1-.5-.866V9.072c0-.357.19-.688.5-.866l12-6.929a1.003 1.003 0 0 1 1 0l12 6.929a1 1 0 0 1 .5.866Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="filled-with-icons-database-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M3.071 8.5C3.071 4.977 8.991 2 16 2s12.929 2.977 12.929 6.5S23.009 15 16 15 3.071 12.023 3.071 8.5Zm0 4.312V16c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 15.336 21.589 17 16 17S5.632 15.336 3.071 12.812Zm0 7.5V23.5c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 22.835 21.589 24.5 16 24.5S5.632 22.836 3.071 20.312Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Filled box example

```html
<div
  class="pf-v6-c-tabs pf-m-fill pf-m-box"
  aria-label="Filled box example"
  role="region"
  id="filled-box"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul class="pf-v6-c-tabs__list" role="tablist" aria-label="Filled box example">
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="filled-box-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="filled-box-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="filled-box-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Filled box with icons example

```html
<div
  class="pf-v6-c-tabs pf-m-fill pf-m-box"
  aria-label="Filled box with icons example"
  role="region"
  id="filled-box-with-icons"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Filled box with icons example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="filled-box-with-icons-users-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M13.766 21.75H2c-.402 0-.748-.317-.75-.718-.013-3.743 2.34-6.941 5.642-8.201A5.747 5.747 0 0 1 4.25 8a5.76 5.76 0 0 1 6.992-5.619c2.167.456 3.918 2.207 4.376 4.373a5.754 5.754 0 0 1-2.51 6.077c.394.15.77.334 1.134.539.103.058.148.18.113.292a7.924 7.924 0 0 0 .807 6.473.237.237 0 0 1-.054.312c-.485.394-.929.835-1.342 1.303Zm11.342-.919A5.747 5.747 0 0 0 27.75 16c0-3.171-2.58-5.75-5.75-5.75s-5.75 2.579-5.75 5.75a5.747 5.747 0 0 0 2.642 4.831c-3.293 1.257-5.642 4.44-5.642 8.169 0 .414.336.75.75.75h16a.75.75 0 0 0 .75-.75c0-3.73-2.349-6.912-5.642-8.169Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="filled-box-with-icons-containers-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29 9.072v13.855c0 .357-.19.688-.5.866l-12 6.929a1 1 0 0 1-1 0l-12-6.929a1 1 0 0 1-.5-.866V9.072c0-.357.19-.688.5-.866l12-6.929a1.003 1.003 0 0 1 1 0l12 6.929a1 1 0 0 1 .5.866Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="filled-box-with-icons-database-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M3.071 8.5C3.071 4.977 8.991 2 16 2s12.929 2.977 12.929 6.5S23.009 15 16 15 3.071 12.023 3.071 8.5Zm0 4.312V16c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 15.336 21.589 17 16 17S5.632 15.336 3.071 12.812Zm0 7.5V23.5c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 22.835 21.589 24.5 16 24.5S5.632 22.836 3.071 20.312Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Filled usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-m-fill`  | `.pf-v6-c-tabs` | Modifies the tabs to fill the available space. **Required** |

## Tabs as navigation

### Using the nav element example

```html
<nav
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Using nav element example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Using nav element example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="false"
        id="using-the-nav-element-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="true"
        id="using-the-nav-element-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="false"
        id="using-the-nav-element-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </a>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link pf-m-disabled"
        aria-disabled="true"
        tabindex="-1"
        href="#"
        role="tab"
        aria-selected="false"
        id="using-the-nav-element-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        href="#"
        role="tab"
        aria-selected="false"
        id="using-the-nav-element-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="false"
        id="using-the-nav-element-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </a>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</nav>

```

### Sub tabs using the nav element example

```html
<nav
  class="pf-v6-c-tabs"
  aria-label="Using nav element with sub tabs example, primary"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Using nav element with sub tabs example, primary"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="false"
        id="sub-tabs-using-the-nav-element-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="true"
        id="sub-tabs-using-the-nav-element-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="false"
        id="sub-tabs-using-the-nav-element-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </a>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="false"
        id="sub-tabs-using-the-nav-element-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="false"
        id="sub-tabs-using-the-nav-element-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="false"
        id="sub-tabs-using-the-nav-element-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </a>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</nav>

<nav
  class="pf-v6-c-tabs pf-m-subtab"
  aria-label="Using nav element with sub tabs example, Containers"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Using nav element with sub tabs example, Containers"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="false"
        id="sub-tabs-using-the-nav-element-subtab-sub-1-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 1</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="false"
        id="sub-tabs-using-the-nav-element-subtab-sub-2-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 2</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="true"
        id="sub-tabs-using-the-nav-element-subtab-sub-3-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 3</span>
      </a>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link pf-m-disabled"
        aria-disabled="true"
        tabindex="-1"
        href="#"
        role="tab"
        aria-selected="false"
        id="sub-tabs-using-the-nav-element-subtab-sub-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        href="#"
        role="tab"
        aria-selected="false"
        id="sub-tabs-using-the-nav-element-subtab-sub-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </a>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <a
        class="pf-v6-c-tabs__link"
        href="#"
        role="tab"
        aria-selected="false"
        id="sub-tabs-using-the-nav-element-subtab-sub-6-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 6</span>
      </a>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</nav>

```

### Site navigation variation

```html isBeta
<nav
  class="pf-v6-c-tabs pf-m-nav"
  aria-label="Site navigation variation example"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-small pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Site navigation variation example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="nav-tabs-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="nav-tabs-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="nav-tabs-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="nav-tabs-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="nav-tabs-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="nav-tabs-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-small pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</nav><br/ >
As sub navigation:
<nav
  class="pf-v6-c-tabs pf-m-subtab pf-m-nav"
  aria-label="Site navigation variation as sub tabs example"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-small pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Site navigation variation as sub tabs example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="nav-tabs-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="nav-tabs-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="nav-tabs-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="nav-tabs-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="nav-tabs-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="nav-tabs-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-small pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</nav>

```

## Tab item actions

### Help button example

```html
<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Help button default example"
  role="region"
  id="help-button-default-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help button default example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-default-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-button-default-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-default-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-default-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-button-default-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-default-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-default-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-box pf-m-scrollable"
  aria-label="Help button box example"
  role="region"
  id="help-button-box-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help button box example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-box-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-button-box-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-box-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-box-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-button-box-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-box-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-box-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-box pf-m-secondary pf-m-scrollable"
  aria-label="Help button box secondary variant example"
  role="region"
  id="help-button-box-secondary-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help button box secondary variant example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-box-secondary-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-button-box-secondary-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-box-secondary-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-box-secondary-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-button-box-secondary-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-box-secondary-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-box-secondary-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Help button with icons example"
  role="region"
  id="help-button-icons-text-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help button with icons example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-icons-text-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M13.766 21.75H2c-.402 0-.748-.317-.75-.718-.013-3.743 2.34-6.941 5.642-8.201A5.747 5.747 0 0 1 4.25 8a5.76 5.76 0 0 1 6.992-5.619c2.167.456 3.918 2.207 4.376 4.373a5.754 5.754 0 0 1-2.51 6.077c.394.15.77.334 1.134.539.103.058.148.18.113.292a7.924 7.924 0 0 0 .807 6.473.237.237 0 0 1-.054.312c-.485.394-.929.835-1.342 1.303Zm11.342-.919A5.747 5.747 0 0 0 27.75 16c0-3.171-2.58-5.75-5.75-5.75s-5.75 2.579-5.75 5.75a5.747 5.747 0 0 0 2.642 4.831c-3.293 1.257-5.642 4.44-5.642 8.169 0 .414.336.75.75.75h16a.75.75 0 0 0 .75-.75c0-3.73-2.349-6.912-5.642-8.169Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-button-icons-text-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29 9.072v13.855c0 .357-.19.688-.5.866l-12 6.929a1 1 0 0 1-1 0l-12-6.929a1 1 0 0 1-.5-.866V9.072c0-.357.19-.688.5-.866l12-6.929a1.003 1.003 0 0 1 1 0l12 6.929a1 1 0 0 1 .5.866Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-icons-text-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M3.071 8.5C3.071 4.977 8.991 2 16 2s12.929 2.977 12.929 6.5S23.009 15 16 15 3.071 12.023 3.071 8.5Zm0 4.312V16c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 15.336 21.589 17 16 17S5.632 15.336 3.071 12.812Zm0 7.5V23.5c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 22.835 21.589 24.5 16 24.5S5.632 22.836 3.071 20.312Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-icons-text-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29.5 9h-27C1.673 9 1 9.673 1 10.5v11c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-11c0-.827-.673-1.5-1.5-1.5ZM13 17.125H8a1.125 1.125 0 0 1 0-2.25h5a1.125 1.125 0 0 1 0 2.25Zm10.005.766a1.874 1.874 0 1 1-.001-3.749 1.874 1.874 0 0 1 .001 3.749Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-button-icons-text-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31 27a1 1 0 0 1-1 1H2a1 1 0 1 1 0-2h28a1 1 0 0 1 1 1ZM3 21.5v-16C3 4.673 3.673 4 4.5 4h23c.827 0 1.5.673 1.5 1.5v16c0 .827-.673 1.5-1.5 1.5h-23c-.827 0-1.5-.673-1.5-1.5ZM14.25 8a1.75 1.75 0 1 0 3.5 0 1.75 1.75 0 0 0-3.5 0Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-icons-text-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M30 29a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1Zm-15.061-4.646c.292.292.676.438 1.061.438s.768-.146 1.061-.438l8.646-8.646a.999.999 0 1 0-1.414-1.414L17 21.587V3a1 1 0 0 0-2 0v18.586l-7.293-7.293a.999.999 0 1 0-1.414 1.414l8.646 8.646Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-icons-text-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M30 3.5v3c0 .827-.673 1.5-1.5 1.5h-25C2.673 8 2 7.327 2 6.5v-3C2 2.673 2.673 2 3.5 2h25c.827 0 1.5.673 1.5 1.5ZM8.75 22.25h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1Zm10 0h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1Zm10 0h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1ZM16 10a1 1 0 0 0-1 1v3H6.5c-.827 0-1.5.673-1.5 1.5V19a1 1 0 1 0 2 0v-3h8v3a1 1 0 1 0 2 0v-3h8v3a1 1 0 1 0 2 0v-3.5c0-.827-.673-1.5-1.5-1.5H17v-3a1 1 0 0 0-1-1Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-fill"
  aria-label="Help button filled example"
  role="region"
  id="help-button-filled-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help button filled example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-filled-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-button-filled-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-filled-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Help button with sub tabs example, primary"
  role="region"
  id="help-button-secondary-primary-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help button with sub tabs example, primary"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-secondary-primary-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-button-secondary-primary-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-secondary-primary-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-secondary-primary-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-button-secondary-primary-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-secondary-primary-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-secondary-primary-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>
<div
  class="pf-v6-c-tabs pf-m-subtab pf-m-scrollable"
  aria-label="Help button with sub tabs example, Containers"
  role="region"
  id="help-button-secondary-secondary-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help button with sub tabs example, Containers"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-secondary-secondary-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-button-secondary-secondary-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-secondary-secondary-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-secondary-secondary-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-button-secondary-secondary-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-button-secondary-secondary-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-button-secondary-secondary-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Close button example

```html
<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Close button default example"
  role="region"
  id="close-button-default-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Close button default example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-default-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="close-button-default-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-default-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-default-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="close-button-default-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-default-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-default-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-box pf-m-scrollable"
  aria-label="Close button box example"
  role="region"
  id="close-button-box-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Close button box example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-box-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="close-button-box-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-box-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-box-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="close-button-box-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-box-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-box-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-box pf-m-secondary pf-m-scrollable"
  aria-label="Close button box secondary variant example"
  role="region"
  id="close-button-box-secondary-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Close button box secondary variant example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-box-secondary-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="close-button-box-secondary-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-box-secondary-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-box-secondary-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="close-button-box-secondary-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-box-secondary-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-box-secondary-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Close button with icons example"
  role="region"
  id="close-button-icons-text-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Close button with icons example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-icons-text-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M13.766 21.75H2c-.402 0-.748-.317-.75-.718-.013-3.743 2.34-6.941 5.642-8.201A5.747 5.747 0 0 1 4.25 8a5.76 5.76 0 0 1 6.992-5.619c2.167.456 3.918 2.207 4.376 4.373a5.754 5.754 0 0 1-2.51 6.077c.394.15.77.334 1.134.539.103.058.148.18.113.292a7.924 7.924 0 0 0 .807 6.473.237.237 0 0 1-.054.312c-.485.394-.929.835-1.342 1.303Zm11.342-.919A5.747 5.747 0 0 0 27.75 16c0-3.171-2.58-5.75-5.75-5.75s-5.75 2.579-5.75 5.75a5.747 5.747 0 0 0 2.642 4.831c-3.293 1.257-5.642 4.44-5.642 8.169 0 .414.336.75.75.75h16a.75.75 0 0 0 .75-.75c0-3.73-2.349-6.912-5.642-8.169Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="close-button-icons-text-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29 9.072v13.855c0 .357-.19.688-.5.866l-12 6.929a1 1 0 0 1-1 0l-12-6.929a1 1 0 0 1-.5-.866V9.072c0-.357.19-.688.5-.866l12-6.929a1.003 1.003 0 0 1 1 0l12 6.929a1 1 0 0 1 .5.866Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-icons-text-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M3.071 8.5C3.071 4.977 8.991 2 16 2s12.929 2.977 12.929 6.5S23.009 15 16 15 3.071 12.023 3.071 8.5Zm0 4.312V16c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 15.336 21.589 17 16 17S5.632 15.336 3.071 12.812Zm0 7.5V23.5c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 22.835 21.589 24.5 16 24.5S5.632 22.836 3.071 20.312Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-icons-text-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29.5 9h-27C1.673 9 1 9.673 1 10.5v11c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-11c0-.827-.673-1.5-1.5-1.5ZM13 17.125H8a1.125 1.125 0 0 1 0-2.25h5a1.125 1.125 0 0 1 0 2.25Zm10.005.766a1.874 1.874 0 1 1-.001-3.749 1.874 1.874 0 0 1 .001 3.749Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="close-button-icons-text-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31 27a1 1 0 0 1-1 1H2a1 1 0 1 1 0-2h28a1 1 0 0 1 1 1ZM3 21.5v-16C3 4.673 3.673 4 4.5 4h23c.827 0 1.5.673 1.5 1.5v16c0 .827-.673 1.5-1.5 1.5h-23c-.827 0-1.5-.673-1.5-1.5ZM14.25 8a1.75 1.75 0 1 0 3.5 0 1.75 1.75 0 0 0-3.5 0Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-icons-text-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-icons-text-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M30 3.5v3c0 .827-.673 1.5-1.5 1.5h-25C2.673 8 2 7.327 2 6.5v-3C2 2.673 2.673 2 3.5 2h25c.827 0 1.5.673 1.5 1.5ZM8.75 22.25h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1Zm10 0h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1Zm10 0h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1ZM16 10a1 1 0 0 0-1 1v3H6.5c-.827 0-1.5.673-1.5 1.5V19a1 1 0 1 0 2 0v-3h8v3a1 1 0 1 0 2 0v-3h8v3a1 1 0 1 0 2 0v-3.5c0-.827-.673-1.5-1.5-1.5H17v-3a1 1 0 0 0-1-1Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-fill"
  aria-label="Close button filled example"
  role="region"
  id="close-button-filled-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Close button filled example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-filled-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="close-button-filled-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-filled-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Close button with sub tabs example, primary"
  role="region"
  id="close-button-secondary-primary-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Close button with sub tabs example, primary"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-secondary-primary-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="close-button-secondary-primary-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-secondary-primary-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-secondary-primary-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="close-button-secondary-primary-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-secondary-primary-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-secondary-primary-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>
<div
  class="pf-v6-c-tabs pf-m-subtab pf-m-scrollable"
  aria-label="Close button with sub tabs example, Containers"
  role="region"
  id="close-button-secondary-secondary-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Close button with sub tabs example, Containers"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-secondary-secondary-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="close-button-secondary-secondary-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-secondary-secondary-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-secondary-secondary-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="close-button-secondary-secondary-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="close-button-secondary-secondary-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="close-button-secondary-secondary-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Help and close button example

```html
<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Help and close button default example"
  role="region"
  id="help-close-button-default-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help and close button default example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-default-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-close-button-default-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-default-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-default-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-close-button-default-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-default-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help disabled"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-default-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Close disabled label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-default-example-help-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help and close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help and close disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help and close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-default-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-box pf-m-scrollable"
  aria-label="Help and close button box example"
  role="region"
  id="help-close-button-box-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help and close button box example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-box-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-close-button-box-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-box-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-box-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-close-button-box-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-box-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help disabled"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-box-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Close disabled label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-box-example-help-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help and close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help and close disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help and close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-box-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-box pf-m-secondary pf-m-scrollable"
  aria-label="Help and close button box secondary variant example"
  role="region"
  id="help-close-button-box-secondary-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help and close button box secondary variant example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-box-secondary-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-close-button-box-secondary-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-box-secondary-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-box-secondary-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-close-button-box-secondary-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-box-secondary-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help disabled"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-box-secondary-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Close disabled label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-box-secondary-example-help-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help and close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help and close disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help and close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-box-secondary-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Help and close button with icons example"
  role="region"
  id="help-close-button-icons-text-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help and close button with icons example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-icons-text-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M13.766 21.75H2c-.402 0-.748-.317-.75-.718-.013-3.743 2.34-6.941 5.642-8.201A5.747 5.747 0 0 1 4.25 8a5.76 5.76 0 0 1 6.992-5.619c2.167.456 3.918 2.207 4.376 4.373a5.754 5.754 0 0 1-2.51 6.077c.394.15.77.334 1.134.539.103.058.148.18.113.292a7.924 7.924 0 0 0 .807 6.473.237.237 0 0 1-.054.312c-.485.394-.929.835-1.342 1.303Zm11.342-.919A5.747 5.747 0 0 0 27.75 16c0-3.171-2.58-5.75-5.75-5.75s-5.75 2.579-5.75 5.75a5.747 5.747 0 0 0 2.642 4.831c-3.293 1.257-5.642 4.44-5.642 8.169 0 .414.336.75.75.75h16a.75.75 0 0 0 .75-.75c0-3.73-2.349-6.912-5.642-8.169Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-close-button-icons-text-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29 9.072v13.855c0 .357-.19.688-.5.866l-12 6.929a1 1 0 0 1-1 0l-12-6.929a1 1 0 0 1-.5-.866V9.072c0-.357.19-.688.5-.866l12-6.929a1.003 1.003 0 0 1 1 0l12 6.929a1 1 0 0 1 .5.866Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-icons-text-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M3.071 8.5C3.071 4.977 8.991 2 16 2s12.929 2.977 12.929 6.5S23.009 15 16 15 3.071 12.023 3.071 8.5Zm0 4.312V16c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 15.336 21.589 17 16 17S5.632 15.336 3.071 12.812Zm0 7.5V23.5c0 3.523 5.92 6.5 12.929 6.5s12.929-2.977 12.929-6.5v-3.188C26.368 22.835 21.589 24.5 16 24.5S5.632 22.836 3.071 20.312Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-icons-text-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M29.5 9h-27C1.673 9 1 9.673 1 10.5v11c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-11c0-.827-.673-1.5-1.5-1.5ZM13 17.125H8a1.125 1.125 0 0 1 0-2.25h5a1.125 1.125 0 0 1 0 2.25Zm10.005.766a1.874 1.874 0 1 1-.001-3.749 1.874 1.874 0 0 1 .001 3.749Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-close-button-icons-text-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31 27a1 1 0 0 1-1 1H2a1 1 0 1 1 0-2h28a1 1 0 0 1 1 1ZM3 21.5v-16C3 4.673 3.673 4 4.5 4h23c.827 0 1.5.673 1.5 1.5v16c0 .827-.673 1.5-1.5 1.5h-23c-.827 0-1.5-.673-1.5-1.5ZM14.25 8a1.75 1.75 0 1 0 3.5 0 1.75 1.75 0 0 0-3.5 0Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-icons-text-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M30 29a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1Zm-15.061-4.646c.292.292.676.438 1.061.438s.768-.146 1.061-.438l8.646-8.646a.999.999 0 1 0-1.414-1.414L17 21.587V3a1 1 0 0 0-2 0v18.586l-7.293-7.293a.999.999 0 1 0-1.414 1.414l8.646 8.646Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help disabled"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-icons-text-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Close disabled label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-icons-text-example-help-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31 9.5v17c0 .827-.673 1.5-1.5 1.5h-27c-.827 0-1.5-.673-1.5-1.5v-17C1 8.673 1.673 8 2.5 8h2.69l.681-3.208A1 1 0 0 1 6.85 4h9.301a1 1 0 0 1 .979.792L17.811 8h11.69c.827 0 1.5.673 1.5 1.5Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Help and close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help and close disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help and close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-icons-text-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M30 3.5v3c0 .827-.673 1.5-1.5 1.5h-25C2.673 8 2 7.327 2 6.5v-3C2 2.673 2.673 2 3.5 2h25c.827 0 1.5.673 1.5 1.5ZM8.75 22.25h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1Zm10 0h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1Zm10 0h-5.5a1 1 0 0 0-1 1v5.5a1 1 0 0 0 1 1h5.5a1 1 0 0 0 1-1v-5.5a1 1 0 0 0-1-1ZM16 10a1 1 0 0 0-1 1v3H6.5c-.827 0-1.5.673-1.5 1.5V19a1 1 0 1 0 2 0v-3h8v3a1 1 0 1 0 2 0v-3h8v3a1 1 0 1 0 2 0v-3.5c0-.827-.673-1.5-1.5-1.5H17v-3a1 1 0 0 0-1-1Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-fill"
  aria-label="Help and close button filled example"
  role="region"
  id="help-close-button-filled-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help and close button filled example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-filled-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-close-button-filled-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-filled-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Help and close button with sub tabs example, primary"
  role="region"
  id="help-close-button-secondary-primary-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help and close button with sub tabs example, primary"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-primary-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-close-button-secondary-primary-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-primary-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-primary-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-primary-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-primary-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help disabled"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-primary-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Close disabled label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-primary-example-help-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help and close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help and close disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help and close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-primary-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>
<div
  class="pf-v6-c-tabs pf-m-subtab pf-m-scrollable"
  aria-label="Help and close button with sub tabs example, Containers"
  role="region"
  id="help-close-button-secondary-secondary-example"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Help and close button with sub tabs example, Containers"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-secondary-example-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Users label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="help-close-button-secondary-secondary-example-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Containers label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-secondary-example-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Database label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-secondary-example-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-secondary-example-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="More info for ARIA disabled label"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-aria-disabled pf-m-plain"
          type="button"
          aria-label="Close ARIA disabled"
          aria-disabled="true"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-secondary-example-help-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help disabled"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-secondary-example-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Close disabled label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li
      class="pf-v6-c-tabs__item pf-m-action pf-m-disabled"
      role="presentation"
    >
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-secondary-example-help-close-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Help and close disabled</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Help and close disabled label"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Help and close disabled"
          disabled
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="help-close-button-secondary-secondary-example-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="More info for Network label"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 32 32"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>

      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

## Add tab button

### Add tab button example

```html
<div
  class="pf-v6-c-tabs pf-m-scrollable"
  aria-label="Add button with sub tabs example, primary"
  role="region"
  id="default-tabs-add-tab-button"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Add button with sub tabs example, primary"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-add-tab-button-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="default-tabs-add-tab-button-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-add-tab-button-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-add-tab-button-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Server"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-add-tab-button-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close System"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-add-tab-button-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <span class="pf-v6-c-tabs__add">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Add tab"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 448 512"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z"
          />
        </svg>
      </span>
    </button>
  </span>
</div>
<div
  class="pf-v6-c-tabs pf-m-subtab pf-m-scrollable"
  aria-label="Add button with sub tabs example, Containers"
  role="region"
  id="default-tabs-add-tab-button-subtab"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Add button with sub tabs example, Containers"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-add-tab-button-subtab-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="default-tabs-add-tab-button-subtab-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-add-tab-button-subtab-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-add-tab-button-subtab-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Server"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-add-tab-button-subtab-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close System"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="default-tabs-add-tab-button-subtab-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <span class="pf-v6-c-tabs__add">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Add tab"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 448 512"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z"
          />
        </svg>
      </span>
    </button>
  </span>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-box pf-m-scrollable"
  aria-label="Add button box example"
  role="region"
  id="box-tabs-add-tab-button"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Add button box example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-add-tab-button-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="box-tabs-add-tab-button-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-add-tab-button-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-add-tab-button-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Server"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-add-tab-button-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close System"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-add-tab-button-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <span class="pf-v6-c-tabs__add">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Add tab"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 448 512"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z"
          />
        </svg>
      </span>
    </button>
  </span>
</div>

<br />
<br />

<div
  class="pf-v6-c-tabs pf-m-box pf-m-secondary pf-m-scrollable"
  aria-label="Add button box secondary variant example"
  role="region"
  id="box-tabs-add-tab-button-secondary "
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Add button box secondary variant example"
  >
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-add-tab-button-secondary -users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Users"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="true"
        id="box-tabs-add-tab-button-secondary -containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Containers"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-add-tab-button-secondary -database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Database"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>

    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-add-tab-button-secondary -server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Server"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-add-tab-button-secondary -system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close System"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-action" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        role="tab"
        aria-selected="false"
        id="box-tabs-add-tab-button-secondary -network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
      <span class="pf-v6-c-tabs__item-action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Close Network"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-tabs__item-action-icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </span>
        </button>
      </span>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <span class="pf-v6-c-tabs__add">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Add tab"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 448 512"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M416 208H272V64c0-17.67-14.33-32-32-32h-32c-17.67 0-32 14.33-32 32v144H32c-17.67 0-32 14.33-32 32v32c0 17.67 14.33 32 32 32h144v144c0 17.67 14.33 32 32 32h32c17.67 0 32-14.33 32-32V304h144c17.67 0 32-14.33 32-32v-32c0-17.67-14.33-32-32-32z"
          />
        </svg>
      </span>
    </button>
  </span>
</div>

```

## Animate current tab accent

To animate the current tab accent, you must set the following variables on the `.pf-v6-c-tabs` wrapper. As tabs are added, removed, and resized, these values may need to be updated dynamically. The following examples use static values for these variables and are not updated dynamically, so there may be styling issues. For more functional examples, see the [react tabs component examples](/components/tabs).

* `--pf-v6-c-tabs--link-accent--start` - the left offset of the current tab
* `--pf-v6-c-tabs--link-accent--length` - the width of the current tab

### Animate default tabs accent

```html
<div
  class="pf-v6-c-tabs pf-m-animate-current"
  style="--pf-v6-c-tabs--link-accent--start: 0px; --pf-v6-c-tabs--link-accent--length: 67px;"
  aria-label="Animate default example"
  role="region"
  id="tabs-animate-current-default"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Animate default example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-default-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="true"
        id="tabs-animate-current-default-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-default-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        onclick="
                  const doc = document.querySelector('html');
                  let isRTL = doc.dir === 'rtl' ? true : false;
                  event.preventDefault();
                  ((e) => {
                    const el = this,
                          li = this.closest('li'),
                          ul = this.closest('ul'),
                          tabs = this.closest('.pf-v6-c-tabs'),
                          top = Math.round(li.offsetTop),
                          width = Math.round(li.offsetWidth),
                          height = Math.round(li.offsetHeight);
                    
                    let left = Math.round(li.offsetLeft);
              
                    const getRight = () => {
                      return ul.offsetWidth - left - width;
                    }
                    
                    left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
              
                    ul.querySelectorAll('li').forEach(function(el) {
                      el.classList.remove('pf-m-current')});
                      li.classList.add('pf-m-current');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                    }
                  )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-default-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        onclick="
                  const doc = document.querySelector('html');
                  let isRTL = doc.dir === 'rtl' ? true : false;
                  event.preventDefault();
                  ((e) => {
                    const el = this,
                          li = this.closest('li'),
                          ul = this.closest('ul'),
                          tabs = this.closest('.pf-v6-c-tabs'),
                          top = Math.round(li.offsetTop),
                          width = Math.round(li.offsetWidth),
                          height = Math.round(li.offsetHeight);
                    
                    let left = Math.round(li.offsetLeft);
              
                    const getRight = () => {
                      return ul.offsetWidth - left - width;
                    }
                    
                    left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
              
                    ul.querySelectorAll('li').forEach(function(el) {
                      el.classList.remove('pf-m-current')});
                      li.classList.add('pf-m-current');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                    }
                  )()"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-default-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
                const doc = document.querySelector('html');
                let isRTL = doc.dir === 'rtl' ? true : false;
                event.preventDefault();
                ((e) => {
                  const el = this,
                        li = this.closest('li'),
                        ul = this.closest('ul'),
                        tabs = this.closest('.pf-v6-c-tabs'),
                        top = Math.round(li.offsetTop),
                        width = Math.round(li.offsetWidth),
                        height = Math.round(li.offsetHeight);
                  
                  let left = Math.round(li.offsetLeft);
            
                  const getRight = () => {
                    return ul.offsetWidth - left - width;
                  }
                  
                  left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
            
                  ul.querySelectorAll('li').forEach(function(el) {
                    el.classList.remove('pf-m-current')});
                    li.classList.add('pf-m-current');
                      tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                      tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                  }
                )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-default-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Animate sub tabs accent

```html
<div
  class="pf-v6-c-tabs pf-m-animate-current pf-m-scrollable"
  style="--pf-v6-c-tabs--link-accent--start: 0px; --pf-v6-c-tabs--link-accent--length: 67px;"
  aria-label="Animate with sub tabs example, primary"
  role="region"
  id="tabs-animate-current-subtabs"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Animate with sub tabs example, primary"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-subtabs-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="true"
        id="tabs-animate-current-subtabs-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-subtabs-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
                  const doc = document.querySelector('html');
                  let isRTL = doc.dir === 'rtl' ? true : false;
                  event.preventDefault();
                  ((e) => {
                    const el = this,
                          li = this.closest('li'),
                          ul = this.closest('ul'),
                          tabs = this.closest('.pf-v6-c-tabs'),
                          top = Math.round(li.offsetTop),
                          width = Math.round(li.offsetWidth),
                          height = Math.round(li.offsetHeight);
                    
                    let left = Math.round(li.offsetLeft);
              
                    const getRight = () => {
                      return ul.offsetWidth - left - width;
                    }
                    
                    left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
              
                    ul.querySelectorAll('li').forEach(function(el) {
                      el.classList.remove('pf-m-current')});
                      li.classList.add('pf-m-current');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                    }
                  )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-subtabs-server-link"
      >
        <span class="pf-v6-c-tabs__item-text">Server</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
                  const doc = document.querySelector('html');
                  let isRTL = doc.dir === 'rtl' ? true : false;
                  event.preventDefault();
                  ((e) => {
                    const el = this,
                          li = this.closest('li'),
                          ul = this.closest('ul'),
                          tabs = this.closest('.pf-v6-c-tabs'),
                          top = Math.round(li.offsetTop),
                          width = Math.round(li.offsetWidth),
                          height = Math.round(li.offsetHeight);
                    
                    let left = Math.round(li.offsetLeft);
              
                    const getRight = () => {
                      return ul.offsetWidth - left - width;
                    }
                    
                    left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
              
                    ul.querySelectorAll('li').forEach(function(el) {
                      el.classList.remove('pf-m-current')});
                      li.classList.add('pf-m-current');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                    }
                  )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-subtabs-system-link"
      >
        <span class="pf-v6-c-tabs__item-text">System</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
                const doc = document.querySelector('html');
                let isRTL = doc.dir === 'rtl' ? true : false;
                event.preventDefault();
                ((e) => {
                  const el = this,
                        li = this.closest('li'),
                        ul = this.closest('ul'),
                        tabs = this.closest('.pf-v6-c-tabs'),
                        top = Math.round(li.offsetTop),
                        width = Math.round(li.offsetWidth),
                        height = Math.round(li.offsetHeight);
                  
                  let left = Math.round(li.offsetLeft);
            
                  const getRight = () => {
                    return ul.offsetWidth - left - width;
                  }
                  
                  left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
            
                  ul.querySelectorAll('li').forEach(function(el) {
                    el.classList.remove('pf-m-current')});
                    li.classList.add('pf-m-current');
                      tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                      tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                  }
                )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-subtabs-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<div
  class="pf-v6-c-tabs pf-m-subtab pf-m-animate-current pf-m-scrollable"
  style="--pf-v6-c-tabs--link-accent--start: 0px; --pf-v6-c-tabs--link-accent--length: 63px;"
  aria-label="Animate with sub tabs example, Users"
  role="region"
  id="tabs-animate-current-subtabs-sub"
>
  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Animate with sub tabs example, Users"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-subtabs-sub-sub-1-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 1</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-subtabs-sub-sub-2-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 2</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="true"
        id="tabs-animate-current-subtabs-sub-sub-3-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 3</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
                  const doc = document.querySelector('html');
                  let isRTL = doc.dir === 'rtl' ? true : false;
                  event.preventDefault();
                  ((e) => {
                    const el = this,
                          li = this.closest('li'),
                          ul = this.closest('ul'),
                          tabs = this.closest('.pf-v6-c-tabs'),
                          top = Math.round(li.offsetTop),
                          width = Math.round(li.offsetWidth),
                          height = Math.round(li.offsetHeight);
                    
                    let left = Math.round(li.offsetLeft);
              
                    const getRight = () => {
                      return ul.offsetWidth - left - width;
                    }
                    
                    left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
              
                    ul.querySelectorAll('li').forEach(function(el) {
                      el.classList.remove('pf-m-current')});
                      li.classList.add('pf-m-current');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                    }
                  )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-subtabs-sub-sub-4-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 4</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
                  const doc = document.querySelector('html');
                  let isRTL = doc.dir === 'rtl' ? true : false;
                  event.preventDefault();
                  ((e) => {
                    const el = this,
                          li = this.closest('li'),
                          ul = this.closest('ul'),
                          tabs = this.closest('.pf-v6-c-tabs'),
                          top = Math.round(li.offsetTop),
                          width = Math.round(li.offsetWidth),
                          height = Math.round(li.offsetHeight);
                    
                    let left = Math.round(li.offsetLeft);
              
                    const getRight = () => {
                      return ul.offsetWidth - left - width;
                    }
                    
                    left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
              
                    ul.querySelectorAll('li').forEach(function(el) {
                      el.classList.remove('pf-m-current')});
                      li.classList.add('pf-m-current');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                    }
                  )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-subtabs-sub-sub-5-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 5</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
                const doc = document.querySelector('html');
                let isRTL = doc.dir === 'rtl' ? true : false;
                event.preventDefault();
                ((e) => {
                  const el = this,
                        li = this.closest('li'),
                        ul = this.closest('ul'),
                        tabs = this.closest('.pf-v6-c-tabs'),
                        top = Math.round(li.offsetTop),
                        width = Math.round(li.offsetWidth),
                        height = Math.round(li.offsetHeight);
                  
                  let left = Math.round(li.offsetLeft);
            
                  const getRight = () => {
                    return ul.offsetWidth - left - width;
                  }
                  
                  left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
            
                  ul.querySelectorAll('li').forEach(function(el) {
                    el.classList.remove('pf-m-current')});
                    li.classList.add('pf-m-current');
                      tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                      tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                  }
                )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-subtabs-sub-sub-6-link"
      >
        <span class="pf-v6-c-tabs__item-text">Item 6</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Animate filled tabs accent

```html
<div
  class="pf-v6-c-tabs pf-m-animate-current pf-m-fill"
  style="--pf-v6-c-tabs--link-accent--start: 0px; --pf-v6-c-tabs--link-accent--length: 253px;"
  aria-label="Animate filled example"
  role="region"
  id="tabs-animate-current-filled"
>
  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll left"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
          />
        </svg>
      </span>
    </button>
  </div>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Animate filled example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-filled-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="true"
        id="tabs-animate-current-filled-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">Containers</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', left + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', width + 'px');
                }
              )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-filled-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>
  </ul>

  <div class="pf-v6-c-tabs__scroll-button" aria-hidden="true">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Scroll right"
      disabled
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 20 20"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Animate vertical tabs accent

```html
<div
  class="pf-v6-c-tabs pf-m-vertical pf-m-animate-current"
  style="--pf-v6-c-tabs--link-accent--start: 8px; --pf-v6-c-tabs--link-accent--length: 45px;"
  aria-label="Animate vertical example"
  role="region"
  id="tabs-animate-current-vertical"
>
  <ul
    class="pf-v6-c-tabs__list"
    role="tablist"
    aria-label="Animate vertical example"
  >
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', top + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', height + 'px');
                }
              )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-vertical-users-link"
      >
        <span class="pf-v6-c-tabs__item-text">Users</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item pf-m-current" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', top + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', height + 'px');
                }
              )()"
        role="tab"
        aria-selected="true"
        id="tabs-animate-current-vertical-containers-link"
      >
        <span class="pf-v6-c-tabs__item-text">
          Containers
          <br />and more
        </span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
              const doc = document.querySelector('html');
              let isRTL = doc.dir === 'rtl' ? true : false;
              event.preventDefault();
              ((e) => {
                const el = this,
                      li = this.closest('li'),
                      ul = this.closest('ul'),
                      tabs = this.closest('.pf-v6-c-tabs'),
                      top = Math.round(li.offsetTop),
                      width = Math.round(li.offsetWidth),
                      height = Math.round(li.offsetHeight);
                
                let left = Math.round(li.offsetLeft);
          
                const getRight = () => {
                  return ul.offsetWidth - left - width;
                }
                
                left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
          
                ul.querySelectorAll('li').forEach(function(el) {
                  el.classList.remove('pf-m-current')});
                  li.classList.add('pf-m-current');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', top + 'px');
                    tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', height + 'px');
                }
              )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-vertical-database-link"
      >
        <span class="pf-v6-c-tabs__item-text">Database</span>
      </button>
    </li>

    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        disabled
        onclick="
                  const doc = document.querySelector('html');
                  let isRTL = doc.dir === 'rtl' ? true : false;
                  event.preventDefault();
                  ((e) => {
                    const el = this,
                          li = this.closest('li'),
                          ul = this.closest('ul'),
                          tabs = this.closest('.pf-v6-c-tabs'),
                          top = Math.round(li.offsetTop),
                          width = Math.round(li.offsetWidth),
                          height = Math.round(li.offsetHeight);
                    
                    let left = Math.round(li.offsetLeft);
              
                    const getRight = () => {
                      return ul.offsetWidth - left - width;
                    }
                    
                    left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
              
                    ul.querySelectorAll('li').forEach(function(el) {
                      el.classList.remove('pf-m-current')});
                      li.classList.add('pf-m-current');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', top + 'px');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', height + 'px');
                    }
                  )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-vertical-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">Disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link pf-m-aria-disabled"
        onclick="
                  const doc = document.querySelector('html');
                  let isRTL = doc.dir === 'rtl' ? true : false;
                  event.preventDefault();
                  ((e) => {
                    const el = this,
                          li = this.closest('li'),
                          ul = this.closest('ul'),
                          tabs = this.closest('.pf-v6-c-tabs'),
                          top = Math.round(li.offsetTop),
                          width = Math.round(li.offsetWidth),
                          height = Math.round(li.offsetHeight);
                    
                    let left = Math.round(li.offsetLeft);
              
                    const getRight = () => {
                      return ul.offsetWidth - left - width;
                    }
                    
                    left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
              
                    ul.querySelectorAll('li').forEach(function(el) {
                      el.classList.remove('pf-m-current')});
                      li.classList.add('pf-m-current');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', top + 'px');
                        tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', height + 'px');
                    }
                  )()"
        aria-disabled="true"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-vertical-aria-disabled-link"
      >
        <span class="pf-v6-c-tabs__item-text">ARIA disabled</span>
      </button>
    </li>
    <li class="pf-v6-c-tabs__item" role="presentation">
      <button
        type="button"
        class="pf-v6-c-tabs__link"
        onclick="
                const doc = document.querySelector('html');
                let isRTL = doc.dir === 'rtl' ? true : false;
                event.preventDefault();
                ((e) => {
                  const el = this,
                        li = this.closest('li'),
                        ul = this.closest('ul'),
                        tabs = this.closest('.pf-v6-c-tabs'),
                        top = Math.round(li.offsetTop),
                        width = Math.round(li.offsetWidth),
                        height = Math.round(li.offsetHeight);
                  
                  let left = Math.round(li.offsetLeft);
            
                  const getRight = () => {
                    return ul.offsetWidth - left - width;
                  }
                  
                  left = isRTL ? getRight(left) : Math.round(li.offsetLeft);
            
                  ul.querySelectorAll('li').forEach(function(el) {
                    el.classList.remove('pf-m-current')});
                    li.classList.add('pf-m-current');
                      tabs.style.setProperty('--pf-v6-c-tabs--link-accent--start', top + 'px');
                      tabs.style.setProperty('--pf-v6-c-tabs--link-accent--length', height + 'px');
                  }
                )()"
        role="tab"
        aria-selected="false"
        id="tabs-animate-current-vertical-network-wired-link"
      >
        <span class="pf-v6-c-tabs__item-text">Network</span>
      </button>
    </li>
  </ul>
</div>

```

## Tab content

### Default tab content example

```html
<section
  class="pf-v6-c-tab-content"
  id="basic-tab1-panel"
  role="tabpanel"
  tabindex="0"
>
  <div class="pf-v6-c-tab-content__body">Panel 1</div>
</section>
<section
  class="pf-v6-c-tab-content"
  id="basic-tab2-panel"
  role="tabpanel"
  tabindex="0"
  hidden
>
  <div class="pf-v6-c-tab-content__body">Panel 2</div>
</section>
<section
  class="pf-v6-c-tab-content"
  id="basic-tab3-panel"
  role="tabpanel"
  tabindex="0"
  hidden
>
  <div class="pf-v6-c-tab-content__body">Panel 3</div>
</section>
<section
  class="pf-v6-c-tab-content"
  id="basic-tab4-panel"
  role="tabpanel"
  tabindex="0"
  hidden
>
  <div class="pf-v6-c-tab-content__body">Panel 4</div>
</section>

```

### Padding

```html
<section
  class="pf-v6-c-tab-content"
  id="tab1-panel-with-padding"
  role="tabpanel"
  tabindex="0"
>
  <div class="pf-v6-c-tab-content__body pf-m-padding">Panel 1</div>
</section>
<section
  class="pf-v6-c-tab-content"
  id="tab2-panel-with-padding"
  role="tabpanel"
  tabindex="0"
  hidden
>
  <div class="pf-v6-c-tab-content__body pf-m-padding">Panel 2</div>
</section>
<section
  class="pf-v6-c-tab-content"
  id="tab3-panel-with-padding"
  role="tabpanel"
  tabindex="0"
  hidden
>
  <div class="pf-v6-c-tab-content__body pf-m-padding">Panel 3</div>
</section>
<section
  class="pf-v6-c-tab-content"
  id="tab4-panel-with-padding"
  role="tabpanel"
  tabindex="0"
  hidden
>
  <div class="pf-v6-c-tab-content__body pf-m-padding">Panel 4</div>
</section>

```

### Secondary

```html
<section
  class="pf-v6-c-tab-content pf-m-secondary"
  id="secondary-tab1-panel"
  role="tabpanel"
  tabindex="0"
>
  <div class="pf-v6-c-tab-content__body">Panel 1</div>
</section>
<section
  class="pf-v6-c-tab-content pf-m-secondary"
  id="secondary-tab2-panel"
  role="tabpanel"
  tabindex="0"
  hidden
>
  <div class="pf-v6-c-tab-content__body">Panel 2</div>
</section>
<section
  class="pf-v6-c-tab-content pf-m-secondary"
  id="secondary-tab3-panel"
  role="tabpanel"
  tabindex="0"
  hidden
>
  <div class="pf-v6-c-tab-content__body">Panel 3</div>
</section>
<section
  class="pf-v6-c-tab-content pf-m-secondary"
  id="secondary-tab4-panel"
  role="tabpanel"
  tabindex="0"
  hidden
>
  <div class="pf-v6-c-tab-content__body">Panel 4</div>
</section>

```

## Documentation

### Tabs overview

The tabs component should only be used to change content views within a page. The similar-looking but semantically different [horizontal nav component](/components/navigation/#horizontal) is available for general navigation use cases.

Whenever a list of tabs is unique on the current page, it can be used in a `<nav>` element. Cases where the same set of tabs are duplicated in multiple regions on a page (e.g. cards on a dashboard) are less likely to benefit from using the `<nav>` element.

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-tabs` | `<nav>`, `<div>` | Initiates the tabs component. **Required** |
| `.pf-v6-c-tabs__list` | `<ul>` | Initiates a tabs component list. **Required** |
| `.pf-v6-c-tabs__item` | `<li>` | Initiates a tabs component item. **Required** |
| `.pf-v6-c-tabs__item-text` | `<span>` | Initiates a tabs component item icon. **Required** |
| `.pf-v6-c-tabs__item-icon` | `<span>` | Initiates a tabs component item text. **Required** |
| `.pf-v6-c-tabs__item-close` | `<span>` | Initiates a tabs component item close. |
| `.pf-v6-c-tabs__item-close-icon` | `<span>` | Initiates a tabs component item close icon. |
| `.pf-v6-c-tabs__link` | `<button>`, `<a>` | Initiates a tabs component link. **Required** |
| `.pf-v6-c-tabs__scroll-button` | `<div>` | Initiates a tabs component scroll button container. |
| `.pf-v6-c-tabs__add` | `<span>` | Initiates a tabs component add button. |
| `.pf-v6-c-tabs__toggle` | `<div>` | Initiates a tabs expandable toggle. |
| `.pf-v6-c-tabs__toggle-button` | `<button>` | Initiates a tabs expandable toggle button. |
| `.pf-v6-c-tabs__toggle-icon` | `<span>` | Initiates a tabs expandable toggle icon. |
| `.pf-v6-c-tabs__toggle-text` | `<span>` | Initiates a tabs expandable toggle text. |
| `.pf-m-subtab` | `.pf-v6-c-tabs` | Applies subtab styling to the tab component. |
| `.pf-m-no-border-bottom` | `.pf-v6-c-tabs` | Removes bottom border from a tab component. |
| `.pf-m-box` | `.pf-v6-c-tabs` | Applies box styling to the tab component. |
| `.pf-m-vertical` | `.pf-v6-c-tabs` | Applies vertical styling to the tab component. |
| `.pf-m-fill` | `.pf-v6-c-tabs` | Modifies the tabs to fill the available space. |
| `.pf-m-inset-{none, sm, md, lg, xl, 2xl}{-on-[md, lg, xl, 2xl]}` | `.pf-v6-c-tabs` | Modifies tabs horizontal padding at optional [breakpoint](/foundations-and-styles/design-tokens/all-design-tokens). |
| `.pf-m-page-insets` | `.pf-v6-c-tabs` | Modifies the tabs component padding/inset to visually match padding of page elements. |
| `.pf-m-secondary` | `.pf-v6-c-tabs.pf-m-box` | Modifies the tabs component tab background colors for the box variant. |
| `.pf-m-expandable{-on-[breakpoint]}` | `.pf-v6-c-tabs` | Modifies the tabs component to be expandable via a toggle at optional [breakpoint](/foundations-and-styles/design-tokens/all-design-tokens). **Note:** works with vertical tabs only. |
| `.pf-m-non-expandable{-on-[breakpoint]}` | `.pf-v6-c-tabs` | Modifies the tabs component to be non-expandable at optional [breakpoint](/foundations-and-styles/design-tokens/all-design-tokens). |
| `.pf-m-expanded` | `.pf-v6-c-tabs` | Modifies the expandable tabs component for the expanded state. |
| `.pf-m-animate-current` | `.pf-v6-c-tabs` | Modifies tabs to animate movement of the current tab accent line. |
| `.pf-m-initializing-accent` | `.pf-v6-c-tabs.pf-m-animate-current` | Modifies tabs styles while initializing the "current" tab's accent styles. |
| `--pf-v6-c-tabs--link-accent--start` | `.pf-v6-c-tabs.pf-m-animate-current` | Sets the value for the "start" inset of the current tab's accent. |
| `--pf-v6-c-tabs--link-accent--length` | `.pf-v6-c-tabs.pf-m-animate-current` | Sets the value for the length of the current tab's accent. |
| `.pf-m-nav` | `.pf-v6-c-tabs` | Applies site navigation styling to the tab component. |
| `.pf-m-current` | `.pf-v6-c-tabs__item` | Indicates that a tab item is currently selected. |
| `.pf-m-action` | `.pf-v6-c-tabs__item` | Indicates that a tab item contains actions other than the tab link. |
| `.pf-m-overflow` | `.pf-v6-c-tabs__item` | Applies overflow menu styling to a tab item. |
| `.pf-m-expanded` | `.pf-v6-c-tabs__item` | Applies expanded styling to the overflow menu tab item. |
| `.pf-m-disabled` | `a.pf-v6-c-tabs__link` | Modifies a tabs link for disabled styles. |
| `.pf-m-aria-disabled` | `.pf-v6-c-tabs__link` | Modifies a tabs link for disabled styles, but is still hoverable/focusable. |

### Tab content accessibility

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `role="tabpanel"` | `.pf-v6-c-tab-content` | Indicates that the element serves as a container for a set of tabs. **Required** |
| `aria-labelledby=[ID of tab element]` | `.pf-v6-c-tab-content` | Provides an accessible name for the tab panel by referring to the tab element that controls it. **Required**
| `id=[ID of tab panel]` | `.pf-v6-c-tab-content` | Provides an ID for the tab panel, and should be used as the value of `aria-controls` on the tab element that controls the panel.  **Required**
| `hidden` | `.pf-v6-c-tab-content` | Indicates that the tab panel is not visible. **Required on all but the active tab panel**
| `tabindex="0"` | `.pf-v6-c-tab-content` | Puts the tab panel in the page tab sequence and facilitates movement to panel content for assistive technology users. **Required**

### Tab content usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-tab-content` | `<section>` |  Initiates the tab content component. **Required** |
| `.pf-v6-c-tab-content__body` | `<div>` |  Initiates the tab content body component. |
| `.pf-m-padding` | `.pf-v6-c-tab-content__body` | Modifies the tab content body component padding. |
| `.pf-m-secondary` | `.pf-v6-c-tab-content` |  Modifies the tab content component for secondary styles. |
