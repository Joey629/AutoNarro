---
id: Inline edit
section: components
cssPrefix: pf-v6-c-inline-edit
---## Introduction

**Inline edit** is a utilitarian component that has two core elements, `.pf-v6-c-inline-edit__value` and `.pf-v6-c-inline-edit__input` and is based on a simple concept. When **value** is visible, **input** is hidden, and vice versa.

### Generic groups

`.pf-v6-c-inline-edit__group`s provide basic layout support and have several available modifiers (`.pf-m-action-group`, `.pf-m-icon-group`).

### Actions

**Actions** (`.pf-v6-c-inline-edit__action`) are hidden by default and exposed when a region of `.pf-v6-c-inline-edit` becomes active. The default visibility of an **action** or **action group** can be inversed by adding `.pf-m-enable-editable`. `.pf-m-enable-editable` flags an element or group of elements as the controlling agents for enabling editable content and therefore is visible by default and hidden when inline editing is enabled.

## Examples

Inline edit **toggle** can be placed anywhere within `.pf-v6-c-inline-edit`. It initiates the editability of elements. When an element becomes editable, **toggle** is hidden.

### Inline edit toggle

```html
<div class="pf-v6-c-inline-edit" id="inline-edit-toggle-example">
  <div class="pf-v6-c-inline-edit__action pf-m-enable-editable">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      id="inline-edit-toggle-example-edit-button"
      aria-label="Edit"
      aria-labelledby="inline-edit-toggle-example-edit-button inline-edit-toggle-example-label"
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
            d="M497.9 142.1l-46.1 46.1c-4.7 4.7-12.3 4.7-17 0l-111-111c-4.7-4.7-4.7-12.3 0-17l46.1-46.1c18.7-18.7 49.1-18.7 67.9 0l60.1 60.1c18.8 18.7 18.8 49.1 0 67.9zM284.2 99.8L21.6 362.4.4 483.9c-2.9 16.4 11.4 30.6 27.8 27.8l121.5-21.3 262.6-262.6c4.7-4.7 4.7-12.3 0-17l-111-111c-4.8-4.7-12.4-4.7-17.1 0zM124.1 339.9c-5.5-5.5-5.5-14.3 0-19.8l154-154c5.5-5.5 14.3-5.5 19.8 0s5.5 14.3 0 19.8l-154 154c-5.5 5.5-14.3 5.5-19.8 0zM88 424h48v36.3l-64.5 11.3-31.1-31.1L51.7 376H88v48z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>

```

Inline edit **value** can be placed anywhere within `.pf-v6-c-inline-edit`. It is visible by default and hidden when inline edit becomes **editable**.

### Inline edit value

```html
<div class="pf-v6-c-inline-edit" id="inline-edit-value-example">
  <div class="pf-v6-c-inline-edit__value">Static value</div>
</div>

```

Inline edit **action-group** contains save and cancel actions and is only visible when inline edit is **editable**.

### Inline edit action group

```html
<div
  class="pf-v6-c-inline-edit pf-m-inline-editable"
  id="inline-edit-action-group-example"
>
  <div class="pf-v6-c-inline-edit__group pf-m-action-group">
    <div class="pf-v6-c-inline-edit__action">
      <button class="pf-v6-c-button pf-m-primary" type="button">
        <span class="pf-v6-c-button__text">Save</span>
      </button>
    </div>
    <div class="pf-v6-c-inline-edit__action">
      <button class="pf-v6-c-button pf-m-secondary" type="button">
        <span class="pf-v6-c-button__text">Cancel</span>
      </button>
    </div>
  </div>
</div>

```

### Inline edit action group icon buttons

```html
<div
  class="pf-v6-c-inline-edit pf-m-inline-editable"
  id="inline-edit-action-group-icon-buttons-example"
>
  <div class="pf-v6-c-inline-edit__group pf-m-action-group pf-m-icon-group">
    <div class="pf-v6-c-inline-edit__action pf-m-valid">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Save edits"
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
    <div class="pf-v6-c-inline-edit__action">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Cancel edits"
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

```

### Single inline edit (default)

```html
<form class="pf-v6-c-inline-edit" id="single-inline-edit-example">
  <div class="pf-v6-c-inline-edit__group">
    <div
      class="pf-v6-c-inline-edit__value"
      id="single-inline-edit-example-label"
    >Static value</div>
    <div class="pf-v6-c-inline-edit__action pf-m-enable-editable">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        id="single-inline-edit-example-edit-button"
        aria-label="Edit"
        aria-labelledby="single-inline-edit-example-edit-button single-inline-edit-example-label"
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
              d="M497.9 142.1l-46.1 46.1c-4.7 4.7-12.3 4.7-17 0l-111-111c-4.7-4.7-4.7-12.3 0-17l46.1-46.1c18.7-18.7 49.1-18.7 67.9 0l60.1 60.1c18.8 18.7 18.8 49.1 0 67.9zM284.2 99.8L21.6 362.4.4 483.9c-2.9 16.4 11.4 30.6 27.8 27.8l121.5-21.3 262.6-262.6c4.7-4.7 4.7-12.3 0-17l-111-111c-4.8-4.7-12.4-4.7-17.1 0zM124.1 339.9c-5.5-5.5-5.5-14.3 0-19.8l154-154c5.5-5.5 14.3-5.5 19.8 0s5.5 14.3 0 19.8l-154 154c-5.5 5.5-14.3 5.5-19.8 0zM88 424h48v36.3l-64.5 11.3-31.1-31.1L51.7 376H88v48z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-inline-edit__group">
    <div class="pf-v6-c-inline-edit__input">
      <span class="pf-v6-c-form-control">
        <input
          type="text"
          value="Static value"
          aria-label="Editable text input"
        />
      </span>
    </div>
    <div class="pf-v6-c-inline-edit__group pf-m-action-group pf-m-icon-group">
      <div class="pf-v6-c-inline-edit__action pf-m-valid">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Save edits"
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
      <div class="pf-v6-c-inline-edit__action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Cancel edits"
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
</form>

```

### Single inline edit (active)

```html
<form
  class="pf-v6-c-inline-edit pf-m-inline-editable"
  id="single-editable-example"
>
  <div class="pf-v6-c-inline-edit__group">
    <div
      class="pf-v6-c-inline-edit__value"
      id="single-editable-example-label"
    >Static value</div>
    <div class="pf-v6-c-inline-edit__action pf-m-enable-editable">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        id="single-editable-example-edit-button"
        aria-label="Edit"
        aria-labelledby="single-editable-example-edit-button single-editable-example-label"
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
              d="M497.9 142.1l-46.1 46.1c-4.7 4.7-12.3 4.7-17 0l-111-111c-4.7-4.7-4.7-12.3 0-17l46.1-46.1c18.7-18.7 49.1-18.7 67.9 0l60.1 60.1c18.8 18.7 18.8 49.1 0 67.9zM284.2 99.8L21.6 362.4.4 483.9c-2.9 16.4 11.4 30.6 27.8 27.8l121.5-21.3 262.6-262.6c4.7-4.7 4.7-12.3 0-17l-111-111c-4.8-4.7-12.4-4.7-17.1 0zM124.1 339.9c-5.5-5.5-5.5-14.3 0-19.8l154-154c5.5-5.5 14.3-5.5 19.8 0s5.5 14.3 0 19.8l-154 154c-5.5 5.5-14.3 5.5-19.8 0zM88 424h48v36.3l-64.5 11.3-31.1-31.1L51.7 376H88v48z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-inline-edit__group">
    <div class="pf-v6-c-inline-edit__input">
      <span class="pf-v6-c-form-control">
        <input
          type="text"
          value="Static value"
          aria-label="Editable text input"
        />
      </span>
    </div>
    <div class="pf-v6-c-inline-edit__group pf-m-action-group pf-m-icon-group">
      <div class="pf-v6-c-inline-edit__action pf-m-valid">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Save edits"
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
      <div class="pf-v6-c-inline-edit__action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Cancel edits"
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
</form>

```

### Free form edit

```html
<div class="pf-v6-c-inline-edit" id="free-form-edit-example">
  <div
    class="pf-v6-c-inline-edit__editable-text"
    role="textbox"
    id="free-form-edit-example-text"
    aria-label="Editable text"
  >Free form text</div>
</div>

```

### Single inline edit with label (default)

```html
<form class="pf-v6-c-inline-edit" id="single-inline-edit-with-label-example">
  <div class="pf-v6-c-inline-edit__group">
    <label
      class="pf-v6-c-inline-edit__label"
      id="single-inline-edit-with-label-example-label"
      for="single-inline-edit-with-label-example-input"
    >Single inline edit group</label>
    <div class="pf-v6-c-inline-edit__action pf-m-enable-editable">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        id="single-inline-edit-with-label-example-edit-button"
        aria-label="Edit"
        aria-labelledby="single-inline-edit-with-label-example-label single-inline-edit-with-label-example-edit-button"
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
              d="M497.9 142.1l-46.1 46.1c-4.7 4.7-12.3 4.7-17 0l-111-111c-4.7-4.7-4.7-12.3 0-17l46.1-46.1c18.7-18.7 49.1-18.7 67.9 0l60.1 60.1c18.8 18.7 18.8 49.1 0 67.9zM284.2 99.8L21.6 362.4.4 483.9c-2.9 16.4 11.4 30.6 27.8 27.8l121.5-21.3 262.6-262.6c4.7-4.7 4.7-12.3 0-17l-111-111c-4.8-4.7-12.4-4.7-17.1 0zM124.1 339.9c-5.5-5.5-5.5-14.3 0-19.8l154-154c5.5-5.5 14.3-5.5 19.8 0s5.5 14.3 0 19.8l-154 154c-5.5 5.5-14.3 5.5-19.8 0zM88 424h48v36.3l-64.5 11.3-31.1-31.1L51.7 376H88v48z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-inline-edit__value">Static value</div>
  <div class="pf-v6-c-inline-edit__group">
    <div class="pf-v6-c-inline-edit__input">
      <span class="pf-v6-c-form-control">
        <input
          type="text"
          id="single-inline-edit-with-label-example-input"
          value="Static value"
          aria-label="Editable text input"
        />
      </span>
    </div>
    <div class="pf-v6-c-inline-edit__group pf-m-action-group pf-m-icon-group">
      <div class="pf-v6-c-inline-edit__action pf-m-valid">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Save edits"
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
      <div class="pf-v6-c-inline-edit__action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Cancel edits"
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
</form>

```

### State valid

```html
<div
  class="pf-v6-c-inline-edit pf-m-inline-editable"
  id="inline-edit-state-valid"
>
  <div class="pf-v6-c-inline-edit__group">
    <label
      class="pf-v6-c-inline-edit__label"
      id="inline-edit-state-valid-label"
      for="inline-edit-state-valid-input"
    >Valid example</label>
    <div class="pf-v6-c-inline-edit__action pf-m-enable-editable">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        id="inline-edit-state-valid-edit-button"
        aria-label="Edit"
        aria-labelledby="inline-edit-state-valid-label inline-edit-state-valid-edit-button"
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
              d="M497.9 142.1l-46.1 46.1c-4.7 4.7-12.3 4.7-17 0l-111-111c-4.7-4.7-4.7-12.3 0-17l46.1-46.1c18.7-18.7 49.1-18.7 67.9 0l60.1 60.1c18.8 18.7 18.8 49.1 0 67.9zM284.2 99.8L21.6 362.4.4 483.9c-2.9 16.4 11.4 30.6 27.8 27.8l121.5-21.3 262.6-262.6c4.7-4.7 4.7-12.3 0-17l-111-111c-4.8-4.7-12.4-4.7-17.1 0zM124.1 339.9c-5.5-5.5-5.5-14.3 0-19.8l154-154c5.5-5.5 14.3-5.5 19.8 0s5.5 14.3 0 19.8l-154 154c-5.5 5.5-14.3 5.5-19.8 0zM88 424h48v36.3l-64.5 11.3-31.1-31.1L51.7 376H88v48z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-inline-edit__value">Static value</div>
  <div class="pf-v6-c-inline-edit__group">
    <div class="pf-v6-c-inline-edit__input">
      <span class="pf-v6-c-form-control">
        <input
          type="text"
          value="Static value"
          aria-label="Editable text input"
        />
      </span>
    </div>
    <div class="pf-v6-c-inline-edit__group pf-m-action-group pf-m-icon-group">
      <div class="pf-v6-c-inline-edit__action pf-m-valid">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Save edits"
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
      <div class="pf-v6-c-inline-edit__action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Cancel edits"
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
</div>

```

### State invalid

```html
<div
  class="pf-v6-c-inline-edit pf-m-inline-editable"
  id="inline-edit-state-invalid"
>
  <div class="pf-v6-c-inline-edit__group">
    <label
      class="pf-v6-c-inline-edit__label"
      id="inline-edit-state-invalid-label"
      for="inline-edit-state-invalid-input"
    >Invalid example</label>
    <div class="pf-v6-c-inline-edit__action pf-m-enable-editable">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        id="inline-edit-state-invalid-edit-button"
        aria-label="Edit"
        aria-labelledby="inline-edit-state-invalid-label inline-edit-state-invalid-edit-button"
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
              d="M497.9 142.1l-46.1 46.1c-4.7 4.7-12.3 4.7-17 0l-111-111c-4.7-4.7-4.7-12.3 0-17l46.1-46.1c18.7-18.7 49.1-18.7 67.9 0l60.1 60.1c18.8 18.7 18.8 49.1 0 67.9zM284.2 99.8L21.6 362.4.4 483.9c-2.9 16.4 11.4 30.6 27.8 27.8l121.5-21.3 262.6-262.6c4.7-4.7 4.7-12.3 0-17l-111-111c-4.8-4.7-12.4-4.7-17.1 0zM124.1 339.9c-5.5-5.5-5.5-14.3 0-19.8l154-154c5.5-5.5 14.3-5.5 19.8 0s5.5 14.3 0 19.8l-154 154c-5.5 5.5-14.3 5.5-19.8 0zM88 424h48v36.3l-64.5 11.3-31.1-31.1L51.7 376H88v48z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-inline-edit__value">Static value</div>
  <div class="pf-v6-c-inline-edit__group">
    <div class="pf-v6-c-inline-edit__input">
      <span class="pf-v6-c-form-control pf-m-required pf-m-error">
        <input
          required
          value="Invalid state"
          aria-invalid="true"
          aria-label="Error state input example"
        />
        <span class="pf-v6-c-form-control__utilities">
          <span class="pf-v6-c-form-control__icon pf-m-status">
            <i class="fas fa-exclamation-circle" aria-hidden="true"></i>
          </span>
        </span>
      </span>
    </div>
    <div class="pf-v6-c-inline-edit__group pf-m-action-group pf-m-icon-group">
      <div class="pf-v6-c-inline-edit__action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          disabled
          aria-label="Save edits"
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
      <div class="pf-v6-c-inline-edit__action">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Cancel edits"
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
</div>

```

### Inline edit table row

```html
<form class="pf-v6-c-inline-edit" id="bulk-edit-table-example">
  <table
    class="pf-v6-c-table pf-m-grid-lg"
    role="grid"
    aria-label="Inline edit table row example"
    id="inline-edit-table-row-example"
  >
    <caption class="pf-v6-c-table__caption">This is the table caption</caption>

    <thead class="pf-v6-c-table__thead">
      <tr class="pf-v6-c-table__tr" role="row">
        <th class="pf-v6-c-table__th" role="columnheader">Text input</th>

        <th class="pf-v6-c-table__th" role="columnheader">Disabled text input</th>

        <th class="pf-v6-c-table__th" role="columnheader">Checkboxes</th>

        <th class="pf-v6-c-table__th" role="columnheader">Radios</th>

        <th class="pf-v6-c-table__th" role="columnheader">Number</th>

        <th
          class="pf-v6-c-table__th pf-v6-c-table__cell-empty"
          role="columnheader"
          scope="col"
        >
          <span class="pf-v6-screen-reader">Actions</span>
        </th>

        <th
          class="pf-v6-c-table__th pf-v6-c-table__cell-empty"
          role="columnheader"
          scope="col"
        >
          <span class="pf-v6-screen-reader">Actions</span>
        </th>
      </tr>
    </thead>

    <tbody class="pf-v6-c-table__tbody" role="rowgroup">
      <tr class="pf-v6-c-table__tr pf-m-inline-editable" role="row">
        <th
          class="pf-v6-c-table__th"
          role="columnheader"
          data-label="Text input"
        >
          <div class="pf-v6-c-inline-edit__value">Text input description content</div>
          <div class="pf-v6-c-inline-edit__input">
            <span class="pf-v6-c-form-control">
              <input
                type="text"
                value="Text input description content"
                id="bulk-edit-table-example-row-1-text-input"
                aria-label="Text input for row 1"
              />
            </span>
          </div>
        </th>

        <td
          class="pf-v6-c-table__td"
          role="cell"
          data-label="Disabled text input"
        >
          <div
            class="pf-v6-c-inline-edit__value"
          >Text input disabled, description content</div>
          <div class="pf-v6-c-inline-edit__input">
            <span class="pf-v6-c-form-control pf-m-disabled">
              <input
                disabled
                type="text"
                value="Text input disabled, description content"
                id="bulk-edit-table-example-row-1-text-input-disabled"
                aria-label="Disabled text input for row 1"
              />
            </span>
          </div>
        </td>
        <td class="pf-v6-c-table__td" role="cell" data-label="Checkboxes">
          <div class="pf-v6-c-inline-edit__value">Check 1, Check 2</div>
          <div
            class="pf-v6-c-inline-edit__group pf-m-column"
            role="group"
            aria-label="Checkbox group for row 1"
          >
            <div class="pf-v6-c-inline-edit__input">
              <div class="pf-v6-c-check">
                <input
                  class="pf-v6-c-check__input"
                  type="checkbox"
                  id="bulk-edit-table-example-row-1-check-1"
                  name="bulk-edit-table-example-row-1-example-check"
                />

                <label
                  class="pf-v6-c-check__label"
                  for="bulk-edit-table-example-row-1-check-1"
                >Check 1</label>
              </div>
            </div>
            <div class="pf-v6-c-inline-edit__input">
              <div class="pf-v6-c-check">
                <input
                  class="pf-v6-c-check__input"
                  type="checkbox"
                  id="bulk-edit-table-example-row-1-check-2"
                  name="bulk-edit-table-example-row-1-example-check-2"
                />

                <label
                  class="pf-v6-c-check__label"
                  for="bulk-edit-table-example-row-1-check-2"
                >Check 2</label>
              </div>
            </div>
          </div>
        </td>
        <td class="pf-v6-c-table__td" role="cell" data-label="Radios">
          <div class="pf-v6-c-inline-edit__value">Radio 1, Radio 2</div>
          <div
            class="pf-v6-c-inline-edit__group pf-m-column"
            role="radiogroup"
            aria-label="Radio group for row 1"
          >
            <div class="pf-v6-c-inline-edit__input">
              <div class="pf-v6-c-radio">
                <input
                  class="pf-v6-c-radio__input"
                  type="radio"
                  id="bulk-edit-table-example-row-1-radio-1"
                  name="bulk-edit-table-example-row-1-example-radio"
                />

                <label
                  class="pf-v6-c-radio__label"
                  for="bulk-edit-table-example-row-1-radio-1"
                >Radio 1</label>
              </div>
            </div>
            <div class="pf-v6-c-inline-edit__input">
              <div class="pf-v6-c-radio">
                <input
                  class="pf-v6-c-radio__input"
                  type="radio"
                  id="bulk-edit-table-example-row-1-radio-2"
                  name="bulk-edit-table-example-row-1-example-radio"
                />

                <label
                  class="pf-v6-c-radio__label"
                  for="bulk-edit-table-example-row-1-radio-2"
                >Radio 2</label>
              </div>
            </div>
          </div>
        </td>
        <td class="pf-v6-c-table__td" role="cell" data-label="Number">
          <div class="pf-v6-c-inline-edit__value">2</div>
          <div class="pf-v6-c-inline-edit__input">
            <span class="pf-v6-c-form-control">
              <input
                type="number"
                value="2"
                id="bulk-edit-table-example-row-1-number-input"
                aria-label="Number input for row 1"
              />
            </span>
          </div>
        </td>
        <td
          class="pf-v6-c-table__td pf-v6-c-table__inline-edit-action"
          role="cell"
        >
          <div
            class="pf-v6-c-inline-edit__group pf-m-action-group pf-m-icon-group"
          >
            <div class="pf-v6-c-inline-edit__action pf-m-valid">
              <button
                class="pf-v6-c-button pf-m-plain"
                type="button"
                aria-label="Save edits"
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
            <div class="pf-v6-c-inline-edit__action">
              <button
                class="pf-v6-c-button pf-m-plain"
                type="button"
                aria-label="Cancel edits"
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
          <div class="pf-v6-c-inline-edit__action pf-m-enable-editable">
            <button
              class="pf-v6-c-button pf-m-plain"
              type="button"
              id="bulk-edit-table-example-row-1-edit-button"
              aria-label="Edit"
              aria-labelledby="bulk-edit-table-example-label bulk-edit-table-example-row-1-edit-button"
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
                    d="M497.9 142.1l-46.1 46.1c-4.7 4.7-12.3 4.7-17 0l-111-111c-4.7-4.7-4.7-12.3 0-17l46.1-46.1c18.7-18.7 49.1-18.7 67.9 0l60.1 60.1c18.8 18.7 18.8 49.1 0 67.9zM284.2 99.8L21.6 362.4.4 483.9c-2.9 16.4 11.4 30.6 27.8 27.8l121.5-21.3 262.6-262.6c4.7-4.7 4.7-12.3 0-17l-111-111c-4.8-4.7-12.4-4.7-17.1 0zM124.1 339.9c-5.5-5.5-5.5-14.3 0-19.8l154-154c5.5-5.5 14.3-5.5 19.8 0s5.5 14.3 0 19.8l-154 154c-5.5 5.5-14.3 5.5-19.8 0zM88 424h48v36.3l-64.5 11.3-31.1-31.1L51.7 376H88v48z"
                  />
                </svg>
              </span>
            </button>
          </div>
        </td>

        <td class="pf-v6-c-table__td pf-v6-c-table__action">
          <button
            class="pf-v6-c-menu-toggle pf-m-plain"
            type="button"
            aria-expanded="false"
            aria-label="Table actions"
          >
            <span class="pf-v6-c-menu-toggle__icon">
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
        </td>
      </tr>

      <tr class="pf-v6-c-table__tr" role="row">
        <th
          class="pf-v6-c-table__th"
          role="columnheader"
          data-label="Text input"
        >
          <div class="pf-v6-c-inline-edit__value">Text input description content</div>
          <div class="pf-v6-c-inline-edit__input">
            <span class="pf-v6-c-form-control">
              <input
                type="text"
                value="Text input description content"
                id="bulk-edit-table-example-row-2-text-input"
                aria-label="Text input for row 2"
              />
            </span>
          </div>
        </th>

        <td
          class="pf-v6-c-table__td"
          role="cell"
          data-label="Disabled text input"
        >
          <div
            class="pf-v6-c-inline-edit__value"
          >Text input disabled, description content</div>
          <div class="pf-v6-c-inline-edit__input">
            <span class="pf-v6-c-form-control pf-m-disabled">
              <input
                disabled
                type="text"
                value="Text input disabled, description content"
                id="bulk-edit-table-example-row-2-text-input-disabled"
                aria-label="Disabled text input for row 2"
              />
            </span>
          </div>
        </td>
        <td class="pf-v6-c-table__td" role="cell" data-label="Checkboxes">
          <div class="pf-v6-c-inline-edit__value">Check 1, Check 2</div>
          <div
            class="pf-v6-c-inline-edit__group pf-m-column"
            role="group"
            aria-label="Checkbox group for row 2"
          >
            <div class="pf-v6-c-inline-edit__input">
              <div class="pf-v6-c-check">
                <input
                  class="pf-v6-c-check__input"
                  type="checkbox"
                  id="bulk-edit-table-example-row-2-check-1"
                  name="bulk-edit-table-example-row-2-example-check"
                />

                <label
                  class="pf-v6-c-check__label"
                  for="bulk-edit-table-example-row-2-check-1"
                >Check 1</label>
              </div>
            </div>
            <div class="pf-v6-c-inline-edit__input">
              <div class="pf-v6-c-check">
                <input
                  class="pf-v6-c-check__input"
                  type="checkbox"
                  id="bulk-edit-table-example-row-2-check-2"
                  name="bulk-edit-table-example-row-2-example-check-2"
                />

                <label
                  class="pf-v6-c-check__label"
                  for="bulk-edit-table-example-row-2-check-2"
                >Check 2</label>
              </div>
            </div>
          </div>
        </td>
        <td class="pf-v6-c-table__td" role="cell" data-label="Radios">
          <div class="pf-v6-c-inline-edit__value">Radio 1, Radio 2</div>
          <div
            class="pf-v6-c-inline-edit__group pf-m-column"
            role="radiogroup"
            aria-label="Radio group for row 2"
          >
            <div class="pf-v6-c-inline-edit__input">
              <div class="pf-v6-c-radio">
                <input
                  class="pf-v6-c-radio__input"
                  type="radio"
                  id="bulk-edit-table-example-row-2-radio-1"
                  name="bulk-edit-table-example-row-2-example-radio-1"
                />

                <label
                  class="pf-v6-c-radio__label"
                  for="bulk-edit-table-example-row-2-radio-1"
                >Radio 1</label>
              </div>
            </div>
            <div class="pf-v6-c-inline-edit__input">
              <div class="pf-v6-c-radio">
                <input
                  class="pf-v6-c-radio__input"
                  type="radio"
                  id="bulk-edit-table-example-row-2-radio-2"
                  name="bulk-edit-table-example-row-2-example-radio-2"
                />

                <label
                  class="pf-v6-c-radio__label"
                  for="bulk-edit-table-example-row-2-radio-2"
                >Radio 2</label>
              </div>
            </div>
          </div>
        </td>
        <td class="pf-v6-c-table__td" role="cell" data-label="Number">
          <div class="pf-v6-c-inline-edit__value">2</div>
          <div class="pf-v6-c-inline-edit__input">
            <span class="pf-v6-c-form-control">
              <input
                type="number"
                value="2"
                id="bulk-edit-table-example-row-2-number-input"
                aria-label="Number input for row 2"
              />
            </span>
          </div>
        </td>
        <td
          class="pf-v6-c-table__td pf-v6-c-table__inline-edit-action"
          role="cell"
        >
          <div
            class="pf-v6-c-inline-edit__group pf-m-action-group pf-m-icon-group"
          >
            <div class="pf-v6-c-inline-edit__action pf-m-valid">
              <button
                class="pf-v6-c-button pf-m-plain"
                type="button"
                aria-label="Save edits"
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
            <div class="pf-v6-c-inline-edit__action">
              <button
                class="pf-v6-c-button pf-m-plain"
                type="button"
                aria-label="Cancel edits"
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
          <div class="pf-v6-c-inline-edit__action pf-m-enable-editable">
            <button
              class="pf-v6-c-button pf-m-plain"
              type="button"
              id="bulk-edit-table-example-row-2-edit-button"
              aria-label="Edit"
              aria-labelledby="bulk-edit-table-example-label bulk-edit-table-example-row-2-edit-button"
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
                    d="M497.9 142.1l-46.1 46.1c-4.7 4.7-12.3 4.7-17 0l-111-111c-4.7-4.7-4.7-12.3 0-17l46.1-46.1c18.7-18.7 49.1-18.7 67.9 0l60.1 60.1c18.8 18.7 18.8 49.1 0 67.9zM284.2 99.8L21.6 362.4.4 483.9c-2.9 16.4 11.4 30.6 27.8 27.8l121.5-21.3 262.6-262.6c4.7-4.7 4.7-12.3 0-17l-111-111c-4.8-4.7-12.4-4.7-17.1 0zM124.1 339.9c-5.5-5.5-5.5-14.3 0-19.8l154-154c5.5-5.5 14.3-5.5 19.8 0s5.5 14.3 0 19.8l-154 154c-5.5 5.5-14.3 5.5-19.8 0zM88 424h48v36.3l-64.5 11.3-31.1-31.1L51.7 376H88v48z"
                  />
                </svg>
              </span>
            </button>
          </div>
        </td>

        <td class="pf-v6-c-table__td pf-v6-c-table__action">
          <button
            class="pf-v6-c-menu-toggle pf-m-plain"
            type="button"
            aria-expanded="false"
            aria-label="Table actions"
          >
            <span class="pf-v6-c-menu-toggle__icon">
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
        </td>
      </tr>
    </tbody>
  </table>
</form>

```

## Documentation

### Accessibility

All accessibility requirements for inputs apply to elements within inline edit.

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `id` | `[labelling element]` | Provides a reference for toggle button and/or editable content. |
| `aria-label="descriptive text"` | `.pf-v6-c-inline-edit__toggle > button` | Provides an accessible description for toggle button. **Required** |
| `aria-labelledby="[labelling element] [toggle button id]"` | `.pf-v6-c-inline-edit__toggle > button` | Provides an accessible description for toggle button. **Required** |
| `aria-label="descriptive text"` | `[radio button group]` | Provides an accessible description for radio groups. **Required** |
| `contenteditable="true"` | `.pf-v6-c-inline-edit__editable-text` | Ensures the text node is editable. |
| `role="textbox"` | `.pf-v6-c-inline-edit__editable-text` | Identifies an element that allows the input of free-form text. |
| `role="radiogroup"` | `[radio button group]` | Provides an accessible role for radio buttons groups. **Required** |

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-inline-edit` | `<form>`, `<div>` | Initiates the inline edit component. **Required** |
| `.pf-v6-c-inline-edit__value` | `*` | Initiates an inline edit value. **Required** |
| `.pf-v6-c-inline-edit__input` | `*` | Initiates an inline edit input. **Required** |
| `.pf-v6-c-inline-edit__editable-text` | `*` | Initiates an inline editable text element. |
| `.pf-v6-c-inline-edit__label` | `*` | Initiates an inline edit label. |
| `.pf-v6-c-inline-edit__action` | `*` | Initiates an inline edit action (visible when inline edit region is active). **Required** |
| `.pf-m-inline-editable` | `.pf-v6-c-inline-edit`, `.pf-v6-c-inline-edit [block level element]` | Modifies an inline edit region for editable state. |
| `.pf-m-action-group` | `.pf-v6-c-inline-edit__group` | Modifies group for action group. |
| `.pf-m-icon-group` | `.pf-v6-c-inline-edit__group` | Modifies an action group item spacing. |
| `.pf-m-column` | `.pf-v6-c-inline-edit__group` | Modifies an action group flex direction. |
| `.pf-m-footer` | `.pf-v6-c-inline-edit__group` | Modifies an inline edit group margin-top. |
| `.pf-m-bold` | `.pf-v6-c-inline-edit__label` | Modifies an inline edit label's `font-weight`. |
| `.pf-m-valid` | `.pf-v6-c-inline-edit__action` | Modifies the action button state. |
| `.pf-m-enable-editable` | `.pf-v6-c-inline-edit__action` | Exposes an inline edit action by default. |
