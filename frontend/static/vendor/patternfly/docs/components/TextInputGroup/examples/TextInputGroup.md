---
id: 'Text input group'
section: components
cssPrefix: pf-v6-c-text-input-group
---import './TextInputGroup.css'

## Examples

### Basic

```html
<div class="pf-v6-c-text-input-group">
  <div class="pf-v6-c-text-input-group__main">
    <span class="pf-v6-c-text-input-group__text">
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        value
        aria-label="Basic"
      />
    </span>
  </div>
</div>

```

### Disabled

```html
<div class="pf-v6-c-text-input-group pf-m-disabled">
  <div class="pf-v6-c-text-input-group__main">
    <span class="pf-v6-c-text-input-group__text">
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        disabled
        value="Disabled"
        aria-label="Disabled"
      />
    </span>
  </div>
</div>

```

### Plain

The following example shows a `TextInputGroup` with the `.pf-m-plain` class applied. A plain `TextInputGroup` must only be used when contained in an ancestor that has its own border or background color styling. <br/> <br/>
For the purposes of this example, the `TextInputGroup` is contained in a wrapper with dashed border styling to show where the component is.

```html
<div class="pf-v6-c-text-input-group pf-m-plain">
  <div class="pf-v6-c-text-input-group__main">
    <span class="pf-v6-c-text-input-group__text">
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        value="Text input group with plain styling"
        aria-label="Plain"
      />
    </span>
  </div>
</div>

```

### Utilities and icon with placeholder text

```html
<div class="pf-v6-c-text-input-group">
  <div class="pf-v6-c-text-input-group__main pf-m-icon">
    <span class="pf-v6-c-text-input-group__text">
      <span class="pf-v6-c-text-input-group__icon">
        <i class="fas fa-fw fa-search"></i>
      </span>
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        placeholder="placeholder"
        value
        aria-label="Utilities and icon with placeholder"
      />
    </span>
  </div>
  <div class="pf-v6-c-text-input-group__utilities">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Clear utilities and icon with placeholder example"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### With validation

```html
<div class="pf-v6-c-text-input-group pf-m-success">
  <div class="pf-v6-c-text-input-group__main">
    <span class="pf-v6-c-text-input-group__text">
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        value="Success validation"
        aria-label="Success validation"
      />
      <span class="pf-v6-c-text-input-group__icon pf-m-status">
        <i aria-hidden="true" class="fas fa-check-circle"></i>
      </span>
    </span>
  </div>
</div>
<br />
<div class="pf-v6-c-text-input-group pf-m-warning">
  <div class="pf-v6-c-text-input-group__main pf-m-icon">
    <span class="pf-v6-c-text-input-group__text">
      <span class="pf-v6-c-text-input-group__icon">
        <i class="fas fa-fw fa-search"></i>
      </span>
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        value="Warning validation with icon at start"
        aria-label="Warning validation"
      />
      <span class="pf-v6-c-text-input-group__icon pf-m-status">
        <i aria-hidden="true" class="fas fa-exclamation-triangle"></i>
      </span>
    </span>
  </div>
</div>
<br />
<div class="pf-v6-c-text-input-group pf-m-error">
  <div class="pf-v6-c-text-input-group__main pf-m-icon">
    <span class="pf-v6-c-text-input-group__text">
      <span class="pf-v6-c-text-input-group__icon">
        <i class="fas fa-fw fa-search"></i>
      </span>
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        value="Error validation with icon at start and utilities"
        aria-label="Error validation"
      />
      <span class="pf-v6-c-text-input-group__icon pf-m-status">
        <i aria-hidden="true" class="fas fa-exclamation-circle"></i>
      </span>
    </span>
  </div>
  <div class="pf-v6-c-text-input-group__utilities">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Clear error validation example"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<br />
<div class="pf-v6-c-text-input-group pf-m-error">
  <div class="pf-v6-c-text-input-group__main">
    <span class="pf-v6-c-text-input-group__text">
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        value="Error validation with no icon but with utilities"
        aria-label="Type to filter"
      />
      <span class="pf-v6-c-text-input-group__icon pf-m-status">
        <i aria-hidden="true" class="fas fa-exclamation-circle"></i>
      </span>
    </span>
  </div>
  <div class="pf-v6-c-text-input-group__utilities">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Clear input"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Filters

```html
<div class="pf-v6-c-text-input-group">
  <div class="pf-v6-c-text-input-group__main">
    <div class="pf-v6-c-label-group">
      <div class="pf-v6-c-label-group__main">
        <ul
          class="pf-v6-c-label-group__list"
          role="list"
          aria-label="Label group list"
        >
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-label-group-label-one-text"
                >Label one</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-label-group-label-one-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-label-group-label-one-button text-input-group-filters-label-group-label-one-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-label-group-label-two-text"
                >Label two</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-label-group-label-two-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-label-group-label-two-button text-input-group-filters-label-group-label-two-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-label-group-label-three-text"
                >Label three</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-label-group-label-three-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-label-group-label-three-button text-input-group-filters-label-group-label-three-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-label-group-label-four-text"
                >Label four</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-label-group-label-four-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-label-group-label-four-button text-input-group-filters-label-group-label-four-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-label-group-label-five-text"
                >Label five</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-label-group-label-five-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-label-group-label-five-button text-input-group-filters-label-group-label-five-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-label-group-label-six-text"
                >Label six</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-label-group-label-six-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-label-group-label-six-button text-input-group-filters-label-group-label-six-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <button class="pf-v6-c-label pf-m-overflow">
              <span class="pf-v6-c-label__content">
                <span class="pf-v6-c-label__content">
                  <span class="pf-v6-c-label__text">8 more</span>
                </span>
              </span>
            </button>
          </li>
        </ul>
      </div>
    </div>
    <span class="pf-v6-c-text-input-group__text">
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        value
        aria-label="Filters"
      />
    </span>
  </div>
  <div class="pf-v6-c-text-input-group__utilities">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Clear filter example"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Filters expanded

```html
<div class="pf-v6-c-text-input-group">
  <div class="pf-v6-c-text-input-group__main">
    <div class="pf-v6-c-label-group">
      <div class="pf-v6-c-label-group__main">
        <ul
          class="pf-v6-c-label-group__list"
          role="list"
          aria-label="Label group list"
        >
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-one-text"
                >Label one</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-one-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-one-button text-input-group-filters-expanded-label-group-label-one-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-two-text"
                >Label two</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-two-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-two-button text-input-group-filters-expanded-label-group-label-two-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-three-text"
                >Label three</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-three-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-three-button text-input-group-filters-expanded-label-group-label-three-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-four-text"
                >Label four</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-four-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-four-button text-input-group-filters-expanded-label-group-label-four-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-five-text"
                >Label five</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-five-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-five-button text-input-group-filters-expanded-label-group-label-five-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-six-text"
                >Label six</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-six-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-six-button text-input-group-filters-expanded-label-group-label-six-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-seven-text"
                >Label seven</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-seven-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-seven-button text-input-group-filters-expanded-label-group-label-seven-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-eight-text"
                >Label eight</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-eight-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-eight-button text-input-group-filters-expanded-label-group-label-eight-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-nine-text"
                >Label nine</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-nine-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-nine-button text-input-group-filters-expanded-label-group-label-nine-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-ten-text"
                >Label ten</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-ten-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-ten-button text-input-group-filters-expanded-label-group-label-ten-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-eleven-text"
                >Label eleven</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-eleven-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-eleven-button text-input-group-filters-expanded-label-group-label-eleven-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-twelve-text"
                >Label twelve</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-twelve-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-twelve-button text-input-group-filters-expanded-label-group-label-twelve-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-thirteen-text"
                >Label thirteen</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-thirteen-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-thirteen-button text-input-group-filters-expanded-label-group-label-thirteen-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
          <li class="pf-v6-c-label-group__list-item">
            <span class="pf-v6-c-label pf-m-outline">
              <span class="pf-v6-c-label__content">
                <span
                  class="pf-v6-c-label__text"
                  id="text-input-group-filters-expanded-label-group-label-fourteen-text"
                >Label fourteen</span>
              </span>
              <span class="pf-v6-c-label__actions">
                <button
                  class="pf-v6-c-button pf-m-no-padding pf-m-plain"
                  type="button"
                  id="text-input-group-filters-expanded-label-group-label-fourteen-button"
                  aria-label="Remove"
                  aria-labelledby="text-input-group-filters-expanded-label-group-label-fourteen-button text-input-group-filters-expanded-label-group-label-fourteen-text"
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
                        d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                      />
                    </svg>
                  </span>
                </button>
              </span>
            </span>
          </li>
        </ul>
      </div>
    </div>
    <span class="pf-v6-c-text-input-group__text">
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        value
        aria-label="Filters expanded"
      />
    </span>
  </div>
  <div class="pf-v6-c-text-input-group__utilities">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Clear filters expanded example"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Autocomplete last option hint

```html
<div class="pf-v6-c-text-input-group">
  <div class="pf-v6-c-text-input-group__main">
    <span class="pf-v6-c-text-input-group__text">
      <input
        class="pf-v6-c-text-input-group__text-input pf-m-hint"
        type="text"
        value="appleseed"
        disabled
        aria-hidden="true"
      />
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        value="apples"
        aria-label="Type to filter"
      />
    </span>
  </div>
</div>

```

### Search input group

The React implementation can be found in the [search input](/components/search-input) component.

```html
<div class="pf-v6-c-text-input-group">
  <div class="pf-v6-c-text-input-group__main pf-m-icon">
    <span class="pf-v6-c-text-input-group__text">
      <span class="pf-v6-c-text-input-group__icon">
        <i class="fas fa-fw fa-search"></i>
      </span>
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        placeholder="Find by name"
        value
        aria-label="Search input group"
      />
    </span>
  </div>
</div>

```

### Search input group, no match

```html
<div class="pf-v6-c-text-input-group">
  <div class="pf-v6-c-text-input-group__main pf-m-icon">
    <span class="pf-v6-c-text-input-group__text">
      <span class="pf-v6-c-text-input-group__icon">
        <i class="fas fa-fw fa-search"></i>
      </span>
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        placeholder="Find by name"
        value="Joh"
        aria-label="Search input group no match"
      />
    </span>
  </div>
  <div class="pf-v6-c-text-input-group__utilities">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Clear search input group no match"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Search input group, match with result count

```html
<div class="pf-v6-c-text-input-group">
  <div class="pf-v6-c-text-input-group__main pf-m-icon">
    <span class="pf-v6-c-text-input-group__text">
      <span class="pf-v6-c-text-input-group__icon">
        <i class="fas fa-fw fa-search"></i>
      </span>
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        placeholder="Find by name"
        value="John Doe"
        aria-label="Search input group match with result count"
      />
    </span>
  </div>
  <div class="pf-v6-c-text-input-group__utilities">
    <span class="pf-v6-c-badge pf-m-read">
      <span aria-hidden="true">3</span>
      <span class="pf-v6-screen-reader">3 matching results</span>
    </span>
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Clear search input group match with result count"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Search input group, match with navigable options

```html
<div class="pf-v6-c-text-input-group">
  <div class="pf-v6-c-text-input-group__main pf-m-icon">
    <span class="pf-v6-c-text-input-group__text">
      <span class="pf-v6-c-text-input-group__icon">
        <i class="fas fa-fw fa-search"></i>
      </span>
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        placeholder="Find by name"
        value="John Doe"
        aria-label="Search input group match with navigable options"
      />
    </span>
  </div>
  <div class="pf-v6-c-text-input-group__utilities">
    <span class="pf-v6-c-badge pf-m-read">
      <span aria-hidden="true">1 / 3</span>
      <span class="pf-v6-screen-reader">Showing result 1 / 3</span>
    </span>
    <div class="pf-v6-c-text-input-group__group">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Previous"
        disabled
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 320 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M177 159.7l136 136c9.4 9.4 9.4 24.6 0 33.9l-22.6 22.6c-9.4 9.4-24.6 9.4-33.9 0L160 255.9l-96.4 96.4c-9.4 9.4-24.6 9.4-33.9 0L7 329.7c-9.4-9.4-9.4-24.6 0-33.9l136-136c9.4-9.5 24.6-9.5 34-.1z"
            />
          </svg>
        </span>
      </button>
      <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Next">
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 320 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M143 352.3L7 216.3c-9.4-9.4-9.4-24.6 0-33.9l22.6-22.6c9.4-9.4 24.6-9.4 33.9 0l96.4 96.4 96.4-96.4c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9l-136 136c-9.2 9.4-24.4 9.4-33.8 0z"
            />
          </svg>
        </span>
      </button>
    </div>
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Clear search input group match with navigable options"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Search input group, expandable

```html
<h3>Collapsed</h3>
<br />
<div class="pf-v6-c-input-group pf-m-search-expandable pf-m-plain">
  <div class="pf-v6-c-input-group__item pf-m-search-input">
    <div class="pf-v6-c-text-input-group">
      <div class="pf-v6-c-text-input-group__main pf-m-icon">
        <span class="pf-v6-c-text-input-group__text">
          <span class="pf-v6-c-text-input-group__icon">
            <i class="fas fa-fw fa-search"></i>
          </span>
          <input
            class="pf-v6-c-text-input-group__text-input"
            type="text"
            placeholder="Search"
            value
            aria-label="Search input group collapsed"
          />
        </span>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-search-expand pf-m-plain">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Open search input group collapsed"
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
            d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-search-action pf-m-plain">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close search input group expandable"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>
<br />
<br />
<h3>Expanded</h3>
<br />
<div
  class="pf-v6-c-input-group pf-m-expanded pf-m-search-expandable pf-m-plain"
>
  <div class="pf-v6-c-input-group__item pf-m-search-input">
    <div class="pf-v6-c-text-input-group">
      <div class="pf-v6-c-text-input-group__main pf-m-icon">
        <span class="pf-v6-c-text-input-group__text">
          <span class="pf-v6-c-text-input-group__icon">
            <i class="fas fa-fw fa-search"></i>
          </span>
          <input
            class="pf-v6-c-text-input-group__text-input"
            type="text"
            placeholder="Search"
            value
            aria-label="Search input group expanded"
          />
        </span>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-search-expand pf-m-plain">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Open search input group collapsed"
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
            d="M505 442.7L405.3 343c-4.5-4.5-10.6-7-17-7H372c27.6-35.3 44-79.7 44-128C416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c48.3 0 92.7-16.4 128-44v16.3c0 6.4 2.5 12.5 7 17l99.7 99.7c9.4 9.4 24.6 9.4 33.9 0l28.3-28.3c9.4-9.4 9.4-24.6.1-34zM208 336c-70.7 0-128-57.2-128-128 0-70.7 57.2-128 128-128 70.7 0 128 57.2 128 128 0 70.7-57.2 128-128 128z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-search-action pf-m-plain">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Close search input group expandable"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Search input group, with submit button

```html
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <div class="pf-v6-c-text-input-group">
      <div class="pf-v6-c-text-input-group__main pf-m-icon">
        <span class="pf-v6-c-text-input-group__text">
          <span class="pf-v6-c-text-input-group__icon">
            <i class="fas fa-fw fa-search"></i>
          </span>
          <input
            class="pf-v6-c-text-input-group__text-input"
            type="text"
            placeholder="Find by name"
            value
            aria-label="Search input group with submit button"
          />
        </span>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-input-group__item">
    <button
      class="pf-v6-c-button pf-m-control"
      type="submit"
      aria-label="Submit search input group"
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
            d="M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Search input group, advanced search

```html
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <div class="pf-v6-c-text-input-group">
      <div class="pf-v6-c-text-input-group__main pf-m-icon">
        <span class="pf-v6-c-text-input-group__text">
          <span class="pf-v6-c-text-input-group__icon">
            <i class="fas fa-fw fa-search"></i>
          </span>
          <input
            class="pf-v6-c-text-input-group__text-input"
            type="text"
            value="username:root firstname:ned"
            aria-label="Search input group advanced search"
          />
        </span>
      </div>
      <div class="pf-v6-c-text-input-group__utilities">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Clear advance search input group collapsed"
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
                d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
              />
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-input-group__item">
    <button
      class="pf-v6-c-button pf-m-control"
      type="button"
      aria-expanded="false"
      aria-label="Advanced search collapsed"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 320 512"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M31.3 192h257.3c17.8 0 26.7 21.5 14.1 34.1L174.1 354.8c-7.8 7.8-20.5 7.8-28.3 0L17.2 226.1C4.6 213.5 13.5 192 31.3 192z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-input-group__item">
    <button
      class="pf-v6-c-button pf-m-control"
      type="submit"
      aria-label="Search advance search input group collapsed"
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
            d="M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

### Search input group, advanced search expanded

```html
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <div class="pf-v6-c-text-input-group">
      <div class="pf-v6-c-text-input-group__main pf-m-icon">
        <span class="pf-v6-c-text-input-group__text">
          <span class="pf-v6-c-text-input-group__icon">
            <i class="fas fa-fw fa-search"></i>
          </span>
          <input
            class="pf-v6-c-text-input-group__text-input"
            type="text"
            value="username:root firstname:ned"
            aria-label="Search input group advanced search expanded"
          />
        </span>
      </div>
      <div class="pf-v6-c-text-input-group__utilities">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Clear advance search input group expanded"
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
                d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
              />
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-input-group__item">
    <button
      class="pf-v6-c-button pf-m-expanded pf-m-control"
      type="button"
      aria-expanded="true"
      aria-label="Advanced search expanded"
    >
      <span class="pf-v6-c-button__icon">
        <svg
          class="pf-v6-svg"
          viewBox="0 0 320 512"
          fill="currentColor"
          aria-hidden="true"
          role="img"
          width="1em"
          height="1em"
        >
          <path
            d="M31.3 192h257.3c17.8 0 26.7 21.5 14.1 34.1L174.1 354.8c-7.8 7.8-20.5 7.8-28.3 0L17.2 226.1C4.6 213.5 13.5 192 31.3 192z"
          />
        </svg>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-input-group__item">
    <button
      class="pf-v6-c-button pf-m-control"
      type="submit"
      aria-label="Search advance search input group expanded"
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
            d="M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<div class="pf-v6-c-panel pf-m-raised">
  <div class="pf-v6-c-panel__main">
    <div class="pf-v6-c-panel__main-body">
      <form class="pf-v6-c-form" novalidate>
        <div class="pf-v6-c-form__group">
          <div class="pf-v6-c-form__group-label"><label
              class="pf-v6-c-form__label"
              for="text-input-group-advanced-search-input-expanded-legacy-form-example-username"
            >
              <span class="pf-v6-c-form__label-text">Username</span></label>
          </div>
          <div class="pf-v6-c-form__group-control">
            <span class="pf-v6-c-form-control">
              <input
                type="text"
                value="root"
                id="text-input-group-advanced-search-input-expanded-legacy-form-example-username"
                name="text-input-group-advanced-search-input-expanded-legacy-form-example-username"
              />
            </span>
          </div>
        </div>
        <div class="pf-v6-c-form__group">
          <div class="pf-v6-c-form__group-label"><label
              class="pf-v6-c-form__label"
              for="text-input-group-advanced-search-input-expanded-legacy-form-example-firstname"
            >
              <span class="pf-v6-c-form__label-text">First name</span></label>
          </div>
          <div class="pf-v6-c-form__group-control">
            <span class="pf-v6-c-form-control">
              <input
                type="text"
                value="ned"
                id="text-input-group-advanced-search-input-expanded-legacy-form-example-firstname"
                name="text-input-group-advanced-search-input-expanded-legacy-form-example-firstname"
              />
            </span>
          </div>
        </div>
        <div class="pf-v6-c-form__group">
          <div class="pf-v6-c-form__group-label"><label
              class="pf-v6-c-form__label"
              for="text-input-group-advanced-search-input-expanded-legacy-form-example-group"
            >
              <span class="pf-v6-c-form__label-text">Group</span></label>
          </div>
          <div class="pf-v6-c-form__group-control">
            <span class="pf-v6-c-form-control">
              <input
                type="text"
                id="text-input-group-advanced-search-input-expanded-legacy-form-example-group"
                name="text-input-group-advanced-search-input-expanded-legacy-form-example-group"
              />
            </span>
          </div>
        </div>
        <div class="pf-v6-c-form__group">
          <div class="pf-v6-c-form__group-label"><label
              class="pf-v6-c-form__label"
              for="text-input-group-advanced-search-input-expanded-legacy-form-example-email"
            >
              <span class="pf-v6-c-form__label-text">Email</span></label>
          </div>
          <div class="pf-v6-c-form__group-control">
            <span class="pf-v6-c-form-control">
              <input
                type="text"
                id="text-input-group-advanced-search-input-expanded-legacy-form-example-email"
                name="text-input-group-advanced-search-input-expanded-legacy-form-example-email"
              />
            </span>
          </div>
        </div>
        <div class="pf-v6-c-form__group pf-m-action">
          <div class="pf-v6-c-form__actions">
            <button
              class="pf-v6-c-button pf-m-primary"
              id="submit-advanced-search-expanded"
              type="submit"
              aria-labelledby="submit-advanced-search-expanded search-input-group-advanced-search-expanded"
            >
              <span class="pf-v6-c-button__text">Submit</span>
            </button>
            <button
              class="pf-v6-c-button pf-m-link"
              id="reset-advanced-search-expanded"
              type="reset"
              aria-labelledby="reset-advanced-search-expanded search-input-group-advanced-search-expanded"
            >
              <span class="pf-v6-c-button__text">Reset</span>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</div>

```

### Search input group, autocomplete

```html
<div class="pf-v6-c-text-input-group">
  <div class="pf-v6-c-text-input-group__main pf-m-icon">
    <span class="pf-v6-c-text-input-group__text">
      <span class="pf-v6-c-text-input-group__icon">
        <i class="fas fa-fw fa-search"></i>
      </span>
      <input
        class="pf-v6-c-text-input-group__text-input"
        type="text"
        value="app"
        aria-label="Search input group autocomplete"
      />
    </span>
  </div>
  <div class="pf-v6-c-text-input-group__utilities">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Clear autocomplete search input group"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<div class="pf-v6-c-menu">
  <div class="pf-v6-c-menu__content">
    <ul class="pf-v6-c-menu__list" role="menu">
      <li class="pf-v6-c-menu__list-item" role="none">
        <button class="pf-v6-c-menu__item" type="button" role="menuitem">
          <span class="pf-v6-c-menu__item-main">
            <span class="pf-v6-c-menu__item-text">apple</span>
          </span>
        </button>
      </li>
      <li class="pf-v6-c-menu__list-item" role="none">
        <button class="pf-v6-c-menu__item" type="button" role="menuitem">
          <span class="pf-v6-c-menu__item-main">
            <span class="pf-v6-c-menu__item-text">appleby</span>
          </span>
        </button>
      </li>
      <li class="pf-v6-c-menu__list-item" role="none">
        <button class="pf-v6-c-menu__item" type="button" role="menuitem">
          <span class="pf-v6-c-menu__item-main">
            <span class="pf-v6-c-menu__item-text">appleseed</span>
          </span>
        </button>
      </li>
      <li class="pf-v6-c-menu__list-item" role="none">
        <button class="pf-v6-c-menu__item" type="button" role="menuitem">
          <span class="pf-v6-c-menu__item-main">
            <span class="pf-v6-c-menu__item-text">appleton</span>
          </span>
        </button>
      </li>
    </ul>
  </div>
</div>

```

### Search input group, autocomplete last option hint

```html
<div class="pf-v6-c-text-input-group">
  <div class="pf-v6-c-text-input-group__main pf-m-icon">
    <span class="pf-v6-c-text-input-group__text">
      <span class="pf-v6-c-text-input-group__icon">
        <i class="fas fa-fw fa-search"></i>
      </span>
      <input
        class="pf-v6-c-text-input-group__text-input pf-m-hint"
        type="text"
        value="appleseed"
        disabled
        aria-hidden="true"
      />
    </span>
  </div>
  <div class="pf-v6-c-text-input-group__utilities">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Clear autocomple search input group last option hint"
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
            d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

<div class="pf-v6-c-menu">
  <div class="pf-v6-c-menu__content">
    <ul class="pf-v6-c-menu__list" role="menu">
      <li class="pf-v6-c-menu__list-item" role="none">
        <button class="pf-v6-c-menu__item" type="button" role="menuitem">
          <span class="pf-v6-c-menu__item-main">
            <span class="pf-v6-c-menu__item-text">appleseed</span>
          </span>
        </button>
      </li>
    </ul>
  </div>
</div>

```

### Search input group, advanced search expanded with autocomplete

```html
<div class="ws-example-wrapper">
  <div class="pf-v6-c-input-group">
    <div class="pf-v6-c-input-group__item pf-m-fill">
      <div class="pf-v6-c-text-input-group">
        <div class="pf-v6-c-text-input-group__main pf-m-icon">
          <span class="pf-v6-c-text-input-group__text">
            <span class="pf-v6-c-text-input-group__icon">
              <i class="fas fa-fw fa-search"></i>
            </span>
            <input
              class="pf-v6-c-text-input-group__text-input"
              type="text"
              value="username:root firstname:n"
              aria-label="Search input group advanced search expanded with autocomplete"
            />
          </span>
        </div>
        <div class="pf-v6-c-text-input-group__utilities">
          <button
            class="pf-v6-c-button pf-m-plain"
            type="button"
            aria-label="Clear advance search input group expanded with autocomplete"
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
                  d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
                />
              </svg>
            </span>
          </button>
        </div>
      </div>
    </div>
    <div class="pf-v6-c-input-group__item">
      <button
        class="pf-v6-c-button pf-m-expanded pf-m-control"
        type="button"
        aria-expanded="true"
        aria-label="Advanced search expanded with autocomplete"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 320 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.3 192h257.3c17.8 0 26.7 21.5 14.1 34.1L174.1 354.8c-7.8 7.8-20.5 7.8-28.3 0L17.2 226.1C4.6 213.5 13.5 192 31.3 192z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-input-group__item">
      <button
        class="pf-v6-c-button pf-m-control"
        type="submit"
        aria-label="Search advanced search input group expanded with autocomplete"
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
              d="M190.5 66.9l22.2-22.2c9.4-9.4 24.6-9.4 33.9 0L441 239c9.4 9.4 9.4 24.6 0 33.9L246.6 467.3c-9.4 9.4-24.6 9.4-33.9 0l-22.2-22.2c-9.5-9.5-9.3-25 .4-34.3L311.4 296H24c-13.3 0-24-10.7-24-24v-32c0-13.3 10.7-24 24-24h287.4L190.9 101.2c-9.8-9.3-10-24.8-.4-34.3z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>

  <div class="pf-v6-c-panel pf-m-raised">
    <div class="pf-v6-c-panel__main">
      <div class="pf-v6-c-panel__main-body">
        <form class="pf-v6-c-form" novalidate>
          <div class="pf-v6-c-form__group">
            <div class="pf-v6-c-form__group-label"><label
                class="pf-v6-c-form__label"
                for="text-input-group-advanced-search-input-form-with-autocomplete-example-username"
              >
                <span class="pf-v6-c-form__label-text">Username</span></label>
            </div>
            <div class="pf-v6-c-form__group-control">
              <span class="pf-v6-c-form-control">
                <input
                  type="text"
                  value="root"
                  id="text-input-group-advanced-search-input-form-with-autocomplete-example-username"
                  name="text-input-group-advanced-search-input-form-with-autocomplete-example-username"
                />
              </span>
            </div>
          </div>
          <div class="pf-v6-c-form__group">
            <div class="pf-v6-c-form__group-label"><label
                class="pf-v6-c-form__label"
                for="text-input-group-advanced-search-input-form-with-autocomplete-example-firstname"
              >
                <span class="pf-v6-c-form__label-text">First name</span></label>
            </div>
            <div class="pf-v6-c-form__group-control">
              <span class="pf-v6-c-form-control">
                <input
                  type="text"
                  value="ned"
                  id="text-input-group-advanced-search-input-form-with-autocomplete-example-firstname"
                  name="text-input-group-advanced-search-input-form-with-autocomplete-example-firstname"
                />
              </span>
            </div>
          </div>
          <div class="pf-v6-c-form__group">
            <div class="pf-v6-c-form__group-label"><label
                class="pf-v6-c-form__label"
                for="text-input-group-advanced-search-input-form-with-autocomplete-example-group"
              >
                <span class="pf-v6-c-form__label-text">Group</span></label>
            </div>
            <div class="pf-v6-c-form__group-control">
              <span class="pf-v6-c-form-control">
                <input
                  type="text"
                  id="text-input-group-advanced-search-input-form-with-autocomplete-example-group"
                  name="text-input-group-advanced-search-input-form-with-autocomplete-example-group"
                />
              </span>
            </div>
          </div>
          <div class="pf-v6-c-form__group">
            <div class="pf-v6-c-form__group-label"><label
                class="pf-v6-c-form__label"
                for="text-input-group-advanced-search-input-form-with-autocomplete-example-email"
              >
                <span class="pf-v6-c-form__label-text">Email</span></label>
            </div>
            <div class="pf-v6-c-form__group-control">
              <span class="pf-v6-c-form-control">
                <input
                  type="text"
                  id="text-input-group-advanced-search-input-form-with-autocomplete-example-email"
                  name="text-input-group-advanced-search-input-form-with-autocomplete-example-email"
                />
              </span>
            </div>
          </div>
          <div class="pf-v6-c-form__group pf-m-action">
            <div class="pf-v6-c-form__actions">
              <button
                class="pf-v6-c-button pf-m-primary"
                id="submit-advanced-search-expanded-with-autocomplete"
                type="submit"
                aria-labelledby="submit-advanced-search-expanded-with-autocomplete search-input-group-advanced-search-expanded-with-autocomplete"
              >
                <span class="pf-v6-c-button__text">Submit</span>
              </button>
              <button
                class="pf-v6-c-button pf-m-link"
                id="reset-advanced-search-expanded-with-autocomplete"
                type="submit"
                aria-labelledby="reset-advanced-search-expanded-with-autocomplete search-input-group-advanced-search-expanded-with-autocomplete"
              >
                <span class="pf-v6-c-button__text">Reset</span>
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>

  <div class="pf-v6-c-menu">
    <div class="pf-v6-c-menu__content">
      <ul class="pf-v6-c-menu__list" role="menu">
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">nancy</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">ned</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">neil</span>
            </span>
          </button>
        </li>
        <li class="pf-v6-c-menu__list-item" role="none">
          <button class="pf-v6-c-menu__item" type="button" role="menuitem">
            <span class="pf-v6-c-menu__item-main">
              <span class="pf-v6-c-menu__item-text">nicole</span>
            </span>
          </button>
        </li>
      </ul>
    </div>
  </div>
</div>

```

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-text-input-group` | `<div>` | Creates a text input group. *Required* |
| `.pf-v6-c-text-input-group__main` | `<div>` | Creates a wrapper for the main content. *Required* |
| `.pf-v6-c-text-input-group__text` | `<span>` | Creates the text container. *Required*|
| `.pf-v6-c-text-input-group__icon` | `<span>` | Creates a container for an icon. |
| `.pf-v6-c-text-input-group__text-input` | `<input>` | Creates a text input. *Required* |
| `.pf-v6-c-text-input-group__utilities` | `<div>` | Creates text input utilities container. |
| `.pf-v6-c-text-input-group__group` | `<div>` | Creates text input prev/next nav group. |
| `.pf-m-plain` | `.pf-v6-c-text-input-group` | Applies plain styling. Only use this variant when the text input group is contained in an ancestor with its own border or background styling. |
| `.pf-m-disabled` | `.pf-v6-c-text-input-group` | Applies disabled styling. The `<input>` should also be `disabled`. |
| `.pf-m-success` | `.pf-v6-c-text-input-group` | Applies success validation styling. |
| `.pf-m-warning` | `.pf-v6-c-text-input-group` | Applies warning validation styling. |
| `.pf-m-error` | `.pf-v6-c-text-input-group` | Applies error validation styling. |
| `.pf-m-icon` | `.pf-v6-c-text-input-group__main` | Applies styling when icons are included in the container. |
| `.pf-m-status` | `.pf-v6-c-text-input-group__icon` | Applies status styling to the icon, matching the status modifier applied to `.pf-v6-c-text-input-group`. |
| `.pf-m-hint` | `.pf-v6-c-text-input-group__text-input` | Applies styling when hints are included in the container. |
