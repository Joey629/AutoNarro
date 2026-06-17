---
id: Action list
section: components
cssPrefix: pf-v6-c-action-list
---## Examples

### Action list single group

```html
<div class="pf-v6-c-action-list">
  <div class="pf-v6-c-action-list__group">
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-primary" type="button">
        <span class="pf-v6-c-button__text">Next</span>
      </button>
    </div>
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-secondary" type="button">
        <span class="pf-v6-c-button__text">Back</span>
      </button>
    </div>
  </div>
</div>
<br />With kebab
<div class="pf-v6-c-action-list">
  <div class="pf-v6-c-action-list__group">
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-primary" type="button">
        <span class="pf-v6-c-button__text">Next</span>
      </button>
    </div>
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-secondary" type="button">
        <span class="pf-v6-c-button__text">Back</span>
      </button>
    </div>
    <div class="pf-v6-c-action-list__item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Toggle"
      >
        <span class="pf-v6-c-button__icon">
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
              d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
</div>

```

### Action list with icons

```html
<div class="pf-v6-c-action-list pf-m-icons">
  <div class="pf-v6-c-action-list__item">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <div class="pf-v6-c-action-list__item">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Toggle">
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
            d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>
<br />With group icons wrapper
<div class="pf-v6-c-action-list">
  <div class="pf-v6-c-action-list__group pf-m-icons">
    <div class="pf-v6-c-action-list__item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon pf-m-start">
          <svg
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
    <div class="pf-v6-c-action-list__item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Toggle"
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
              d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-action-list__group pf-m-icons">
    <div class="pf-v6-c-action-list__item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
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
    <div class="pf-v6-c-action-list__item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Toggle"
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
              d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
</div>

```

### Action list multiple groups

```html
<div class="pf-v6-c-action-list">
  <div class="pf-v6-c-action-list__group">
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-primary" type="button">
        <span class="pf-v6-c-button__text">Next</span>
      </button>
    </div>
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-secondary" type="button">
        <span class="pf-v6-c-button__text">Back</span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-action-list__group">
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-primary" type="button">
        <span class="pf-v6-c-button__text">Submit</span>
      </button>
    </div>
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-link" type="button">
        <span class="pf-v6-c-button__text">Cancel</span>
      </button>
    </div>
  </div>
</div>

```

### Action list with cancel button

```html
In modals, forms, data lists
<div class="pf-v6-c-action-list">
  <div class="pf-v6-c-action-list__group">
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-primary" type="button">
        <span class="pf-v6-c-button__text">Save</span>
      </button>
    </div>
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-link" type="button">
        <span class="pf-v6-c-button__text">Cancel</span>
      </button>
    </div>
  </div>
</div>
<br />In wizards
<div class="pf-v6-c-action-list">
  <div class="pf-v6-c-action-list__group">
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-primary" type="button">
        <span class="pf-v6-c-button__text">Next</span>
      </button>
    </div>
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-secondary" type="button">
        <span class="pf-v6-c-button__text">Back</span>
      </button>
    </div>
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-link" type="button">
        <span class="pf-v6-c-button__text">Cancel</span>
      </button>
    </div>
  </div>
</div>

```

### Vertical action list

```html isBeta
Multiple groups
<div class="pf-v6-c-action-list pf-m-vertical">
  <div class="pf-v6-c-action-list__group">
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-primary" type="button">
        <span class="pf-v6-c-button__text">Next</span>
      </button>
    </div>
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-secondary" type="button">
        <span class="pf-v6-c-button__text">Back</span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-action-list__group">
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-primary" type="button">
        <span class="pf-v6-c-button__text">Submit</span>
      </button>
    </div>
    <div class="pf-v6-c-action-list__item">
      <button class="pf-v6-c-button pf-m-link" type="button">
        <span class="pf-v6-c-button__text">Cancel</span>
      </button>
    </div>
  </div>
</div><br/ >
Icons, in two groups
<div class="pf-v6-c-action-list pf-m-vertical">
  <div class="pf-v6-c-action-list__group pf-m-icons">
    <div class="pf-v6-c-action-list__item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon pf-m-start">
          <svg
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
    <div class="pf-v6-c-action-list__item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Toggle"
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
              d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-action-list__group pf-m-icons">
    <div class="pf-v6-c-action-list__item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
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
    <div class="pf-v6-c-action-list__item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Toggle"
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
              d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
</div>

```

### Overview

### Usage

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-action-list` | `<div>` | Initiates the action list container. |
| `.pf-v6-c-action-list__item` | `<div>` | Initiates the action list item container. |
| `.pf-v6-c-action-list__group` | `<div>` | Initiates the action list group container. |
| `.pf-m-icons` | `.pf-v6-c-action-list`, `.pf-v6-c-action-list__group` | Modifies the action list and/or group to support icon buttons. If applied to `.pf-v6-c-action-list`, all nested groups will inherit this modification. |
| `.pf-m-vertical` | `.pf-v6-c-action-list` | Modifies the action list to display vertically. |
