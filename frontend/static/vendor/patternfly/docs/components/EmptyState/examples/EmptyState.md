---
id: Empty state
section: components
cssPrefix: pf-v6-c-empty-state
---## Examples

### Basic

```html
<div class="pf-v6-c-empty-state">
  <div class="pf-v6-c-empty-state__content">
    <div class="pf-v6-c-empty-state__header">
      <div class="pf-v6-c-empty-state__icon">
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
            d="M488.6 250.2L392 214V105.5c0-15-9.3-28.4-23.4-33.7l-100-37.5c-8.1-3.1-17.1-3.1-25.3 0l-100 37.5c-14.1 5.3-23.4 18.7-23.4 33.7V214l-96.6 36.2C9.3 255.5 0 268.9 0 283.9V394c0 13.6 7.7 26.1 19.9 32.2l100 50c10.1 5.1 22.1 5.1 32.2 0l103.9-52 103.9 52c10.1 5.1 22.1 5.1 32.2 0l100-50c12.2-6.1 19.9-18.6 19.9-32.2V283.9c0-15-9.3-28.4-23.4-33.7zM358 214.8l-85 31.9v-68.2l85-37v73.3zM154 104.1l102-38.2 102 38.2v.6l-102 41.4-102-41.4v-.6zm84 291.1l-85 42.5v-79.1l85-38.8v75.4zm0-112l-102 41.4-102-41.4v-.6l102-38.2 102 38.2v.6zm240 112l-85 42.5v-79.1l85-38.8v75.4zm0-112l-102 41.4-102-41.4v-.6l102-38.2 102 38.2v.6z"
          />
        </svg>
      </div>
      <div class="pf-v6-c-empty-state__title">
        <h4 class="pf-v6-c-empty-state__title-text">Empty state</h4>
      </div>
    </div>

    <div
      class="pf-v6-c-empty-state__body"
    >This represents an the empty state pattern in PatternFly. Hopefully it's simple enough to use but flexible enough to meet a variety of needs.</div>

    <div class="pf-v6-c-empty-state__footer">
      <div class="pf-v6-c-empty-state__actions">
        <button class="pf-v6-c-button pf-m-primary" type="button">
          <span class="pf-v6-c-button__text">Primary action</span>
        </button>
      </div>
      <div class="pf-v6-c-empty-state__actions">
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Multiple</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action buttons</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Can</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Go here</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">In the second</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action area</span>
        </button>
      </div>
    </div>
  </div>
</div>

```

### Extra small

```html
<div class="pf-v6-c-empty-state pf-m-xs">
  <div class="pf-v6-c-empty-state__content">
    <div class="pf-v6-c-empty-state__header">
      <div class="pf-v6-c-empty-state__icon">
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
            d="M488.6 250.2L392 214V105.5c0-15-9.3-28.4-23.4-33.7l-100-37.5c-8.1-3.1-17.1-3.1-25.3 0l-100 37.5c-14.1 5.3-23.4 18.7-23.4 33.7V214l-96.6 36.2C9.3 255.5 0 268.9 0 283.9V394c0 13.6 7.7 26.1 19.9 32.2l100 50c10.1 5.1 22.1 5.1 32.2 0l103.9-52 103.9 52c10.1 5.1 22.1 5.1 32.2 0l100-50c12.2-6.1 19.9-18.6 19.9-32.2V283.9c0-15-9.3-28.4-23.4-33.7zM358 214.8l-85 31.9v-68.2l85-37v73.3zM154 104.1l102-38.2 102 38.2v.6l-102 41.4-102-41.4v-.6zm84 291.1l-85 42.5v-79.1l85-38.8v75.4zm0-112l-102 41.4-102-41.4v-.6l102-38.2 102 38.2v.6zm240 112l-85 42.5v-79.1l85-38.8v75.4zm0-112l-102 41.4-102-41.4v-.6l102-38.2 102 38.2v.6z"
          />
        </svg>
      </div>
      <div class="pf-v6-c-empty-state__title">
        <h4 class="pf-v6-c-empty-state__title-text">Empty state</h4>
      </div>
    </div>

    <div
      class="pf-v6-c-empty-state__body"
    >This represents an the empty state pattern in PatternFly. The icon is optional.</div>

    <div class="pf-v6-c-empty-state__footer">
      <div class="pf-v6-c-empty-state__actions">
        <button class="pf-v6-c-button pf-m-small pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Multiple</span>
        </button>
        <button class="pf-v6-c-button pf-m-small pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action buttons</span>
        </button>
        <button class="pf-v6-c-button pf-m-small pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Can</span>
        </button>
        <button class="pf-v6-c-button pf-m-small pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Go here</span>
        </button>
        <button class="pf-v6-c-button pf-m-small pf-m-link" type="button">
          <span class="pf-v6-c-button__text">In the</span>
        </button>
        <button class="pf-v6-c-button pf-m-small pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action area</span>
        </button>
      </div>
    </div>
  </div>
</div>

```

### Small

```html
<div class="pf-v6-c-empty-state pf-m-sm">
  <div class="pf-v6-c-empty-state__content">
    <div class="pf-v6-c-empty-state__header">
      <div class="pf-v6-c-empty-state__icon">
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
            d="M488.6 250.2L392 214V105.5c0-15-9.3-28.4-23.4-33.7l-100-37.5c-8.1-3.1-17.1-3.1-25.3 0l-100 37.5c-14.1 5.3-23.4 18.7-23.4 33.7V214l-96.6 36.2C9.3 255.5 0 268.9 0 283.9V394c0 13.6 7.7 26.1 19.9 32.2l100 50c10.1 5.1 22.1 5.1 32.2 0l103.9-52 103.9 52c10.1 5.1 22.1 5.1 32.2 0l100-50c12.2-6.1 19.9-18.6 19.9-32.2V283.9c0-15-9.3-28.4-23.4-33.7zM358 214.8l-85 31.9v-68.2l85-37v73.3zM154 104.1l102-38.2 102 38.2v.6l-102 41.4-102-41.4v-.6zm84 291.1l-85 42.5v-79.1l85-38.8v75.4zm0-112l-102 41.4-102-41.4v-.6l102-38.2 102 38.2v.6zm240 112l-85 42.5v-79.1l85-38.8v75.4zm0-112l-102 41.4-102-41.4v-.6l102-38.2 102 38.2v.6z"
          />
        </svg>
      </div>
      <div class="pf-v6-c-empty-state__title">
        <h4 class="pf-v6-c-empty-state__title-text">Empty state</h4>
      </div>
    </div>

    <div
      class="pf-v6-c-empty-state__body"
    >This represents an the empty state pattern in PatternFly. Hopefully it's simple enough to use but flexible enough to meet a variety of needs.</div>

    <div class="pf-v6-c-empty-state__footer">
      <div class="pf-v6-c-empty-state__actions">
        <button class="pf-v6-c-button pf-m-primary" type="button">
          <span class="pf-v6-c-button__text">Primary action</span>
        </button>
      </div>

      <div class="pf-v6-c-empty-state__actions">
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Multiple</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action buttons</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Can</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Go here</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">In the second</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action area</span>
        </button>
      </div>
    </div>
  </div>
</div>

```

### Large

```html
<div class="pf-v6-c-empty-state pf-m-lg">
  <div class="pf-v6-c-empty-state__content">
    <div class="pf-v6-c-empty-state__header">
      <div class="pf-v6-c-empty-state__icon">
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
            d="M488.6 250.2L392 214V105.5c0-15-9.3-28.4-23.4-33.7l-100-37.5c-8.1-3.1-17.1-3.1-25.3 0l-100 37.5c-14.1 5.3-23.4 18.7-23.4 33.7V214l-96.6 36.2C9.3 255.5 0 268.9 0 283.9V394c0 13.6 7.7 26.1 19.9 32.2l100 50c10.1 5.1 22.1 5.1 32.2 0l103.9-52 103.9 52c10.1 5.1 22.1 5.1 32.2 0l100-50c12.2-6.1 19.9-18.6 19.9-32.2V283.9c0-15-9.3-28.4-23.4-33.7zM358 214.8l-85 31.9v-68.2l85-37v73.3zM154 104.1l102-38.2 102 38.2v.6l-102 41.4-102-41.4v-.6zm84 291.1l-85 42.5v-79.1l85-38.8v75.4zm0-112l-102 41.4-102-41.4v-.6l102-38.2 102 38.2v.6zm240 112l-85 42.5v-79.1l85-38.8v75.4zm0-112l-102 41.4-102-41.4v-.6l102-38.2 102 38.2v.6z"
          />
        </svg>
      </div>
      <div class="pf-v6-c-empty-state__title">
        <h4 class="pf-v6-c-empty-state__title-text">Empty state</h4>
      </div>
    </div>

    <div
      class="pf-v6-c-empty-state__body"
    >This represents an the empty state pattern in PatternFly. Hopefully it's simple enough to use but flexible enough to meet a variety of needs.</div>

    <div class="pf-v6-c-empty-state__footer">
      <div class="pf-v6-c-empty-state__actions">
        <button class="pf-v6-c-button pf-m-primary" type="button">
          <span class="pf-v6-c-button__text">Primary action</span>
        </button>
      </div>
      <div class="pf-v6-c-empty-state__actions">
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Multiple</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action buttons</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Can</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Go here</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">In the second</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action area</span>
        </button>
      </div>
    </div>
  </div>
</div>

```

### Extra large

```html
<div class="pf-v6-c-empty-state pf-m-xl">
  <div class="pf-v6-c-empty-state__content">
    <div class="pf-v6-c-empty-state__header">
      <div class="pf-v6-c-empty-state__icon">
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
            d="M488.6 250.2L392 214V105.5c0-15-9.3-28.4-23.4-33.7l-100-37.5c-8.1-3.1-17.1-3.1-25.3 0l-100 37.5c-14.1 5.3-23.4 18.7-23.4 33.7V214l-96.6 36.2C9.3 255.5 0 268.9 0 283.9V394c0 13.6 7.7 26.1 19.9 32.2l100 50c10.1 5.1 22.1 5.1 32.2 0l103.9-52 103.9 52c10.1 5.1 22.1 5.1 32.2 0l100-50c12.2-6.1 19.9-18.6 19.9-32.2V283.9c0-15-9.3-28.4-23.4-33.7zM358 214.8l-85 31.9v-68.2l85-37v73.3zM154 104.1l102-38.2 102 38.2v.6l-102 41.4-102-41.4v-.6zm84 291.1l-85 42.5v-79.1l85-38.8v75.4zm0-112l-102 41.4-102-41.4v-.6l102-38.2 102 38.2v.6zm240 112l-85 42.5v-79.1l85-38.8v75.4zm0-112l-102 41.4-102-41.4v-.6l102-38.2 102 38.2v.6z"
          />
        </svg>
      </div>
      <div class="pf-v6-c-empty-state__title">
        <h4 class="pf-v6-c-empty-state__title-text">Empty state</h4>
      </div>
    </div>

    <div
      class="pf-v6-c-empty-state__body"
    >This represents an the empty state pattern in PatternFly. Hopefully it's simple enough to use but flexible enough to meet a variety of needs.</div>
    <div class="pf-v6-c-empty-state__footer">
      <div class="pf-v6-c-empty-state__actions">
        <button class="pf-v6-c-button pf-m-primary" type="button">
          <span class="pf-v6-c-button__text">Primary action</span>
        </button>
      </div>
      <div class="pf-v6-c-empty-state__actions">
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Multiple</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action buttons</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Can</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Go here</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">In the second</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action area</span>
        </button>
      </div>
    </div>
  </div>
</div>

```

### With status

```html
<div class="pf-v6-c-empty-state pf-m-success">
  <div class="pf-v6-c-empty-state__content">
    <div class="pf-v6-c-empty-state__header">
      <div class="pf-v6-c-empty-state__icon">
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
            d="M504 256c0 136.967-111.033 248-248 248S8 392.967 8 256 119.033 8 256 8s248 111.033 248 248zM227.314 387.314l184-184c6.248-6.248 6.248-16.379 0-22.627l-22.627-22.627c-6.248-6.249-16.379-6.249-22.628 0L216 308.118l-70.059-70.059c-6.248-6.248-16.379-6.248-22.628 0l-22.627 22.627c-6.248 6.248-6.248 16.379 0 22.627l104 104c6.249 6.249 16.379 6.249 22.628.001z"
          />
        </svg>
      </div>
      <div class="pf-v6-c-empty-state__title">
        <h4 class="pf-v6-c-empty-state__title-text">You're all set</h4>
      </div>
    </div>

    <div
      class="pf-v6-c-empty-state__body"
    >This represents an the empty state pattern in PatternFly. Hopefully it's simple enough to use but flexible enough to meet a variety of needs.</div>

    <div class="pf-v6-c-empty-state__footer">
      <div class="pf-v6-c-empty-state__actions">
        <button class="pf-v6-c-button pf-m-primary" type="button">
          <span class="pf-v6-c-button__text">Primary action</span>
        </button>
      </div>
      <div class="pf-v6-c-empty-state__actions">
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Multiple</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action buttons</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Can</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Go here</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">In the second</span>
        </button>
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__text">Action area</span>
        </button>
      </div>
    </div>
  </div>
</div>

```

## Documentation

### Accessibility

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `aria-hidden="true"` | `.pf-v6-c-empty-state__icon` |  Hides icon for assistive technologies. **Required** |

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-empty-state` | `<div>` |  Initiates an empty state component. The empty state centers its content (`.pf-v6-c-empty-state__content`) vertically and horizontally. **Required** |
| `.pf-v6-c-empty-state__content` | `<div>` |  Creates the content container. **Required** |
| `.pf-v6-c-empty-state__header` | `<div>` |  Creates the header container. **Required** |
| `.pf-v6-c-empty-state__title` | `<div>` |  Creates the empty state title container. **Required** |
| `.pf-v6-c-empty-state__title-text` | `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`, `<div>` |  Creates the empty state title text container. |
| `.pf-v6-c-empty-state__icon` | `<div>` |  Creates the empty state icon container. |
| `.pf-v6-c-empty-state__body` | `<div>` |  Creates the empty state body content. There can be more than one `.pf-v6-c-empty-state__body` elements. |
| `.pf-v6-c-empty-state__footer` | `<div>` |  Creates the footer container. **Required** |
| `.pf-v6-c-empty-state__actions` | `<div>` |  Container for actions. **Required** |
| `.pf-m-xs` | `.pf-v6-c-empty-state` | Modifies the empty state for an extra small variation and max-width. |
| `.pf-m-sm` | `.pf-v6-c-empty-state` | Modifies the empty state for a small max-width. |
| `.pf-m-lg` | `.pf-v6-c-empty-state` | Modifies the empty state for a large max-width. |
| `.pf-m-xl` | `.pf-v6-c-empty-state` | Modifies the empty state for an extra large variation and max-width. |
| `.pf-m-full-height` | `.pf-v6-c-empty-state` | Modifies the empty state to be `height: 100%`. If you need the empty state content to be centered vertically, you can use this modifier to make the empty state fill the height of its container, and center `.pf-v6-c-empty-state__content`. **Note:** this modifier requires the parent of `.pf-v6-c-empty-state` have an implicit or explicit `height` defined.  |
| `.pf-m-danger` | `.pf-v6-c-empty-state` | Modifies the empty state for danger status. |
| `.pf-m-warning` | `.pf-v6-c-empty-state` | Modifies the empty state for warning status. |
| `.pf-m-success` | `.pf-v6-c-empty-state` | Modifies the empty state for success status. |
| `.pf-m-info` | `.pf-v6-c-empty-state` | Modifies the empty state for info status. |
| `.pf-m-custom` | `.pf-v6-c-empty-state` | Modifies the empty state for custom status. |
