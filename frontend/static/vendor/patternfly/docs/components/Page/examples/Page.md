---
id: Page
section: components
cssPrefix: pf-v6-c-page
wrapperTag: div
---import './Page.css'

## Examples

### Vertical nav

```html
<div class="pf-v6-c-page">
  <header class="pf-v6-c-masthead">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">Logo</a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <span>Content</span>
    </div>
  </header>
  <div class="pf-v6-c-page__sidebar">
    <div class="pf-v6-c-page__sidebar-main">
      <div class="pf-v6-c-page__sidebar-body">Navigation</div>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main class="pf-v6-c-page__main" tabindex="-1">
      <section
        class="pf-v6-c-page__main-section"
        aria-label="Default main section example 1"
      >
        <div class="pf-v6-c-page__main-body">
          This is a default
          <code>.pf-v6-c-page__main-section</code>.
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-secondary"
        aria-label="Secondary main section example 1"
      >
        <div class="pf-v6-c-page__main-body">
          This
          <code>.pf-v6-c-page__main-section</code> uses
          <code>.pf-m-secondary</code>.
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section"
        aria-label="Default main section example 2"
      >
        <div class="pf-v6-c-page__main-body">
          This is a default
          <code>.pf-v6-c-page__main-section</code>.
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-secondary"
        aria-label="Multiple main body section example"
      >
        <div
          class="pf-v6-c-page__main-body"
        >This is a page__main-body, one of three within one page__main-section.</div>
        <div
          class="pf-v6-c-page__main-body"
        >This is a page__main-body, one of three within one page__main-section.</div>
        <div
          class="pf-v6-c-page__main-body"
        >This is a page__main-body, one of three within one page__main-section.</div>
      </section>
    </main>
  </div>
</div>

```

### Horizontal nav

```html
<div class="pf-v6-c-page">
  <header class="pf-v6-c-masthead">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">Logo</a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <span>Content</span>
    </div>
  </header>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main class="pf-v6-c-page__main" tabindex="-1">
      <section
        class="pf-v6-c-page__main-section"
        aria-label="Horizontal nav default main section example 1"
      >
        <div class="pf-v6-c-page__main-body">
          This is a default
          <code>.pf-v6-c-page__main-section</code>.
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-secondary"
        aria-label="Horizontal nav secondary main section example"
      >
        <div class="pf-v6-c-page__main-body">
          This
          <code>.pf-v6-c-page__main-section</code> uses
          <code>.pf-m-secondary</code>.
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section"
        aria-label="Horizontal nav default main section example 2"
      >
        <div class="pf-v6-c-page__main-body">
          This is a default
          <code>.pf-v6-c-page__main-section</code>.
        </div>
      </section>
    </main>
  </div>
</div>

```

### Multiple sidebar body elements, padding, and fill

```html
<div class="pf-v6-c-page">
  <header class="pf-v6-c-masthead">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">Logo</a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <span>Content</span>
    </div>
  </header>
  <div class="pf-v6-c-page__sidebar">
    <div class="pf-v6-c-page__sidebar-main">
      <div class="pf-v6-c-page__sidebar-body">Navigation</div>
      <div class="pf-v6-c-page__sidebar-body pf-m-fill">inset content</div>
      <div
        class="pf-v6-c-page__sidebar-body pf-m-fill pf-m-inset-none"
      >content that is not inset</div>
      <div class="pf-v6-c-page__sidebar-body pf-m-no-fill">footer content</div>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main class="pf-v6-c-page__main" tabindex="-1">
      <section
        class="pf-v6-c-page__main-section"
        aria-label="Sidebar body layout section"
      >
        <div class="pf-v6-c-page__main-body"></div>
      </section>
    </main>
  </div>
</div>

```

### With or without fill

```html
<div class="pf-v6-c-page">
  <header class="pf-v6-c-masthead">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">Logo</a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <span>Content</span>
    </div>
  </header>
  <div class="pf-v6-c-page__main-container pf-m-fill" tabindex="-1">
    <main class="pf-v6-c-page__main" tabindex="-1">
      <section
        class="pf-v6-c-page__main-section"
        aria-label="Regular page section example"
      >
        <div class="pf-v6-c-page__main-body">A regular page section.</div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-fill"
        aria-label="Fill page section example"
      >
        <div class="pf-v6-c-page__main-body">
          This section uses
          <code>.pf-m-fill</code> to fill the available space. The
          <code>.pf-v6-c-page__main-container</code> must also have
          <code>.pf-m-fill</code> in order for the section to have space to stretch to full height.
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-no-fill"
        aria-label="No fill page section example"
      >
        <div class="pf-v6-c-page__main-body">
          This section uses
          <code>.pf-m-no-fill</code> and will not fill the available space.
        </div>
      </section>
    </main>
  </div>
</div>

```

### Main section padding

```html
<div class="pf-v6-c-page">
  <header class="pf-v6-c-masthead">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">Logo</a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <span>Content</span>
    </div>
  </header>
  <div class="pf-v6-c-page__sidebar">
    <div class="pf-v6-c-page__sidebar-main">
      <div class="pf-v6-c-page__sidebar-body">Navigation</div>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main class="pf-v6-c-page__main" tabindex="-1">
      <section
        class="pf-v6-c-page__main-section"
        aria-label="Default padding main section example"
      >
        <div class="pf-v6-c-page__main-body">
          This
          <code>.pf-v6-c-page__main-section</code> has default padding.
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-no-padding"
        aria-label="No padding main section example"
      >
        <div class="pf-v6-c-page__main-body">
          This
          <code>.pf-v6-c-page__main-section</code> uses
          <code>.pf-m-no-padding</code> to remove all padding.
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-no-padding pf-m-padding-on-md"
        aria-label="Responsive padding main section example"
      >
        <div class="pf-v6-c-page__main-body">
          This
          <code>.pf-v6-c-page__main-section</code> uses
          <code>.pf-m-no-padding .pf-m-padding-on-md</code> to remove padding up to the
          <code>md</code> breakpoint.
        </div>
      </section>
    </main>
  </div>
</div>

```

### Main section variations

```html
<div class="pf-v6-c-page">
  <header class="pf-v6-c-masthead">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">Logo</a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <span>Content</span>
    </div>
  </header>
  <div class="pf-v6-c-page__sidebar">
    <div class="pf-v6-c-page__sidebar-main">
      <div class="pf-v6-c-page__sidebar-body">Navigation</div>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main class="pf-v6-c-page__main" tabindex="-1">
      <section class="pf-v6-c-page__main-subnav">
        <code>.pf-v6-c-page__main-subnav</code> for horizontal subnav navigation
      </section>
      <section class="pf-v6-c-page__main-tabs">
        <code>.pf-v6-c-page__main-tabs</code> for tabs
      </section>
      <div class="pf-v6-c-page__main-group">
        <code>.pf-v6-c-page__main-group</code> for a group of page sections
      </div>
      <section class="pf-v6-c-page__main-breadcrumb">
        <code>.pf-v6-c-page__main-breadcrumb</code> for breadcrumbs
      </section>
      <section
        class="pf-v6-c-page__main-section"
        aria-label="Main section variations example"
      >
        <div class="pf-v6-c-page__main-body">
          <code>.pf-v6-c-page__main-section</code> for main sections
        </div>
      </section>
      <section class="pf-v6-c-page__main-wizard">
        <code>.pf-v6-c-page__main-wizard</code> for wizards
      </section>
    </main>
  </div>
</div>

```

### Centered section

```html
<div class="pf-v6-c-page">
  <header class="pf-v6-c-masthead">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">Logo</a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <span>Content</span>
    </div>
  </header>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main class="pf-v6-c-page__main" tabindex="-1">
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width pf-m-align-center"
        aria-label="Centered section example"
      >
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-c-card">
            <div class="pf-v6-c-card__body">
              When a width limited page section is wider than the value of
              <code>--pf-v6-c-page--section--m-limit-width--MaxWidth</code>, the section will be centered in the main section.
              <br />
              <br />The content in this example is placed in a card to better illustrate how the section behaves when it is centered. A card is not required to center a page section.
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```

### With dock

```html isBeta
<div class="pf-v6-c-page pf-m-docked">
  <div class="pf-v6-c-page__dock">
    <div class="pf-v6-c-page__dock-main">
      <header class="pf-v6-c-masthead pf-m-docked">
        <div class="pf-v6-c-masthead__main">
          <div class="pf-v6-c-masthead__brand">logo</div>
        </div>
        <div class="pf-v6-c-masthead__content">
          <button
            class="pf-v6-c-button pf-m-plain"
            type="button"
            aria-label="Chat"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 512 512"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M448 0H64C28.7 0 0 28.7 0 64v288c0 35.3 28.7 64 64 64h96v84c0 9.8 11.2 15.5 19.1 9.7L304 416h144c35.3 0 64-28.7 64-64V64c0-35.3-28.7-64-64-64z"
                />
              </svg>
            </span>
          </button>
        </div>
      </header>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main class="pf-v6-c-page__main" tabindex="-1">
      <section
        class="pf-v6-c-page__main-section"
        aria-label="Dock main section example"
      >
        <div class="pf-v6-c-page__main-body">
          This is a default
          <code>.pf-v6-c-page__main-section</code>.
        </div>
      </section>
    </main>
  </div>
</div>

```

### Sticky section dynamic

```html
<div class="pf-v6-c-page">
  <header class="pf-v6-c-masthead">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">Logo</a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <span>Content</span>
    </div>
  </header>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main class="pf-v6-c-page__main" tabindex="-1">
      <div
        class="pf-v6-c-page__main-group pf-m-sticky-top-base pf-m-sticky-top-stuck"
      >
        <section class="pf-v6-c-page__main-breadcrumb">Breadcrumb</section>
        <section
          class="pf-v6-c-page__main-section"
          aria-label="Sticky dynamic section title"
        >
          <div class="pf-v6-c-page__main-body">
            This
            <code>.pf-v6-c-page__main-group</code> uses
            <code>.pf-m-sticky-top-base</code> and
            <code>.pf-m-sticky-top-stuck</code> for dynamic sticky positioning with a fade-in background and shadow.
          </div>
        </section>
      </div>
      <section
        class="pf-v6-c-page__main-section"
        aria-label="Sticky dynamic content section"
      >
        <div class="pf-v6-c-page__main-body">Content below the sticky section.</div>
      </section>
    </main>
  </div>
</div>

```

## Documentation

### Overview

This component provides the basic chrome for a page, including sidebar and main areas.

### Accessibility

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `role="main"` | `.pf-v6-c-page__main` | Identifies the element that serves as the main region. |
| `tabindex="-1"` | `.pf-v6-c-page__main` | Allows the main region to receive programmatic focus. **Required** |
| `id="[id]"` | `.pf-v6-c-page__main` | Provides a hook for sending focus to new content. **Required** |
| `tabindex="0"` | `.pf-v6-c-page__main-section.pf-m-overflow-scroll` | If a page section has overflow content that triggers a scrollbar, to ensure that the content is keyboard accessible, the page section must include either a focusable element within the scrollable region or the page section itself must be focusable by adding `tabindex="0"`. |

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-page` | `<div>` | Declares the page component. |
| `.pf-v6-c-page__sidebar` | `<aside>` | Declares the page sidebar. |
| `.pf-v6-c-page__sidebar-body` | `<div>` | Creates a wrapper within the sidebar to hold content. **Note: The last/only `.pf-v6-c-page__sidebar-body` element will grow to fill the available vertical space. You can change this behavior using `.pf-m-fill` and `.pf-m-no-fill`, which are documented below.** |
| `.pf-v6-c-page__main` | `<main>` | Declares the main page area. |
| `.pf-v6-c-page__main-subnav` | `<section>` | Creates a container to nest the horizontal subnav navigation component in the main page area. |
| `.pf-v6-c-page__main-breadcrumb` | `<section>` | Creates a container to nest the breadcrumb component in the main page area. |
| `.pf-v6-c-page__main-section` | `<section>` | Creates a section container in the main page area. **Note: This section will not fill the vertical space. You can change this behavior using `.pf-m-fill` and `.pf-m-no-fill`, which are documented below.**  |
| `.pf-v6-c-page__main-tabs` | `<section>` | Creates a container to nest the tabs component in the main page area. |
| `.pf-v6-c-page__main-wizard` | `<section>` | Creates a container to nest the wizard component in the main page area. |
| `.pf-v6-c-page__main-body` | `<div>` | Creates the body section for a page section. **Required** |
| `.pf-v6-c-page__main-group` | `<div>` | Creates the group of `.pf-v6-c-page__main-*` sections. Can be used in combination with `.pf-m-sticky-[top/bottom]` to make multiple sections sticky. |
| `.pf-v6-c-page__drawer` | `<div>` | Creates a container for the drawer component when placing the main page element in the drawer body. |
| `.pf-m-docked` | `.pf-v6-c-page` | Modifies the page grid to have a dock. |
| `.pf-m-no-sidebar` | `.pf-v6-c-page` | Modifies the page grid for layouts without a sidebar. |
| `.pf-m-expanded` | `.pf-v6-c-page__sidebar` | Modifies the sidebar for the expanded state. |
| `.pf-m-collapsed` | `.pf-v6-c-page__sidebar` | Modifies the sidebar for the collapsed state. |
| `.pf-m-page-insets` | `.pf-v6-c-page__sidebar-body` | Modifies a sidebar body padding/inset to visually match padding of page elements. |
| `.pf-m-context-selector` | `.pf-v6-c-page__sidebar-body` | Modifies a sidebar body to contain a context selector. |
| `.pf-m-inset-none` | `.pf-v6-c-page__sidebar-body` | Removes a sidebar body left/right inset. |
| `.pf-m-padding{-on-[breakpoint]}` | `.pf-v6-c-page__main-section` | Modifies the main page section to add padding back in at an optional [breakpoint](/foundations-and-styles/design-tokens/all-design-tokens). Should be used with pf-m-no-padding. |
| `.pf-m-no-padding{-on-[breakpoint]}` | `.pf-v6-c-page__main-section` | Removes padding from the main page section at an optional [breakpoint](/foundations-and-styles/design-tokens/all-design-tokens). |
| `.pf-m-fill` | `.pf-v6-c-page__main-container`, `.pf-v6-c-page__main-section`, `.pf-v6-c-page__main-group`, `.pf-v6-c-page__main-wizard`, `.pf-v6-c-page__sidebar-body` | Modifies the element to grow to fill the available space. Note that `.pf-v6-c-page__main-container` must also have `.pf-m-fill` applied in order for the section to have space to stretch to full height.|
| `.pf-m-no-fill` | `.pf-v6-c-page__main-section`, `.pf-v6-c-page__main-group`, `.pf-v6-c-page__main-wizard`, `.pf-v6-c-page__sidebar-body` | Modifies the element not to grow to fill the available vertical space. |
| `.pf-m-plain` | `.pf-v6-c-page__main-section`, `.pf-v6-c-page__main-group`, `.pf-v6-c-page__main-wizard`, `.pf-v6-c-page__main-breadcrumb`, `.pf-v6-c-page__main-subnav`, and `.pf-v6-c-page__main-tabs` | Applies plain styling to the section. |
| `.pf-m-no-plain-on-glass` | `.pf-v6-c-page__main-section`, `.pf-v6-c-page__main-group`, `.pf-v6-c-page__main-wizard`, `.pf-v6-c-page__main-breadcrumb`, `.pf-v6-c-page__main-subnav`, and `.pf-v6-c-page__main-tabs` | Prevents the section from automatically applying plain styling when glass theme is enabled. |
| `.pf-m-limit-width` | `.pf-v6-c-page__main-section` | Modifies a page section to limit the `max-width` of the content inside. |
| `.pf-m-align-center` | `.pf-v6-c-page__main-section.pf-m-limit-width` | Modifies a page section body to align center. |
| `.pf-m-sticky-top{-on-[breakpoint]-height}` | `.pf-v6-c-page__main-*` | Modifies a section/group to be sticky to the top of its container at an optional height breakpoint. |
| `.pf-m-sticky-bottom{-on-[breakpoint]-height}` | `.pf-v6-c-page__main-*` | Modifies a section/group to be sticky to the bottom of its container at an optional height breakpoint. |
| `.pf-m-sticky-top-base` | `.pf-v6-c-page__main-*` | Sets up dynamic sticky top positioning with no background or shadow. Used with `.pf-m-sticky-top-stuck`. |
| `.pf-m-sticky-top-stuck` | `.pf-v6-c-page__main-*` | Triggers the sticky top stuck state, fading in the background and shadow. Apply via JS when the section becomes stuck. |
| `.pf-m-sticky-bottom-base` | `.pf-v6-c-page__main-*` | Sets up dynamic sticky bottom positioning with no background or shadow. Used with `.pf-m-sticky-bottom-stuck`. |
| `.pf-m-sticky-bottom-stuck` | `.pf-v6-c-page__main-*` | Triggers the sticky bottom stuck state, fading in the background and shadow. Apply via JS when the section becomes stuck. |
| `.pf-m-shadow-bottom` | `.pf-v6-c-page__main-*` | Modifies a section/group to have a bottom shadow. |
| `.pf-m-shadow-top` | `.pf-v6-c-page__main-*` | Modifies a section/group to have a top shadow. |
| `.pf-m-overflow-scroll` | `.pf-v6-c-page__main-*` | Modifies a section/group to show a scrollbar if it has overflow content. |
