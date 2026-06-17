---
id: Input group
section: components
cssPrefix: pf-v6-c-input-group
---### Overview

Use the input group to extend form controls by adding text, buttons, selects, etc. The input group handles border overlap.

## Examples

### Variations

```html
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item">
    <button
      class="pf-v6-c-button pf-m-control"
      type="button"
      id="textAreaButton1"
    >
      <span class="pf-v6-c-button__text">Button</span>
    </button>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <span class="pf-v6-c-form-control pf-m-textarea pf-m-resize-both">
      <textarea
        name="textarea1"
        id="textarea1"
        aria-label="Textarea with buttons"
        aria-describedby="textAreaButton1"
      ></textarea>
    </span>
  </div>
  <div class="pf-v6-c-input-group__item">
    <button class="pf-v6-c-button pf-m-control" type="button">
      <span class="pf-v6-c-button__text">Button</span>
    </button>
  </div>
</div>
<br />
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <span class="pf-v6-c-form-control pf-m-textarea pf-m-resize-both">
      <textarea
        name="textarea2"
        id="textarea2"
        aria-label="Textarea with button"
        aria-describedby="textAreaButton2"
      ></textarea>
    </span>
  </div>
  <div class="pf-v6-c-input-group__item">
    <button
      class="pf-v6-c-button pf-m-control"
      type="button"
      id="textAreaButton2"
    >
      <span class="pf-v6-c-button__text">Button</span>
    </button>
  </div>
</div>
<br />
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item">
    <button
      class="pf-v6-c-button pf-m-control"
      type="button"
      id="textAreaButton3"
    >
      <span class="pf-v6-c-button__text">Button</span>
    </button>
  </div>
  <div class="pf-v6-c-input-group__item">
    <button class="pf-v6-c-button pf-m-control" type="button">
      <span class="pf-v6-c-button__text">Button</span>
    </button>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <span class="pf-v6-c-form-control pf-m-textarea pf-m-resize-both">
      <textarea
        name="textarea3"
        id="textarea3"
        aria-label="Textarea with buttons"
        aria-describedby="textAreaButton3"
      ></textarea>
    </span>
  </div>
  <div class="pf-v6-c-input-group__item">
    <button class="pf-v6-c-button pf-m-control" type="button">
      <span class="pf-v6-c-button__text">Button</span>
    </button>
  </div>
</div>
<br />
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item">
    <button
      class="pf-v6-c-menu-toggle"
      type="button"
      aria-expanded="false"
      id="select-example-collapsed1"
    >
      <span class="pf-v6-c-menu-toggle__text">Select</span>
      <span class="pf-v6-c-menu-toggle__controls">
        <span class="pf-v6-c-menu-toggle__toggle-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M18.92 5.62C18.77 5.25 18.4 5 18 5H2a1.003 1.003 0 0 0-.71 1.71l7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65c.29-.29.37-.72.22-1.09Z"
            />
          </svg>
        </span>
      </span>
    </button>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <span class="pf-v6-c-form-control">
      <input
        type="text"
        id="textInput4"
        name="textInput4"
        aria-label="Input with select and button"
        aria-describedby="inputSelectButton1"
      />
    </span>
  </div>
  <div class="pf-v6-c-input-group__item">
    <button
      class="pf-v6-c-button pf-m-control"
      type="button"
      id="inputSelectButton1"
    >
      <span class="pf-v6-c-button__text">Button</span>
    </button>
  </div>
</div>
<br />
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item pf-m-box">
    <span class="pf-v6-c-input-group__text">
      <i class="fas fa-dollar-sign" aria-hidden="true"></i>
    </span>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <span class="pf-v6-c-form-control">
      <input
        type="number"
        id="textInput5"
        name="textInput5"
        aria-label=" Dollar amount input example"
      />
    </span>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-box">
    <span class="pf-v6-c-input-group__text">.00</span>
  </div>
</div>
<br />
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <span class="pf-v6-c-form-control">
      <input
        type="email"
        id="textInput6"
        name="textInput6"
        aria-label="Email input field"
        aria-describedby="email-example"
      />
    </span>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-box">
    <span class="pf-v6-c-input-group__text" id="email-example">@example.com</span>
  </div>
</div>
<br />
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item pf-m-box">
    <span class="pf-v6-c-input-group__text">
      <i class="fas fa-at" aria-hidden="true"></i>
    </span>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <span class="pf-v6-c-form-control pf-m-required pf-m-error">
      <input
        required
        type="email"
        id="textInput7"
        name="textInput7"
        aria-invalid="true"
        aria-label="Error state username example"
      />
      <span class="pf-v6-c-form-control__utilities">
        <span class="pf-v6-c-form-control__icon pf-m-status">
          <i class="fas fa-exclamation-circle" aria-hidden="true"></i>
        </span>
      </span>
    </span>
  </div>
</div>
<br />
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <span class="pf-v6-c-form-control">
      <input
        type="text"
        id="textInput13"
        name="textInput13"
        aria-label="Input example with popover"
      />
    </span>
  </div>
  <div class="pf-v6-c-input-group__item">
    <button
      class="pf-v6-c-button pf-m-control"
      type="button"
      aria-label="Popover for input"
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
            d="M504 256c0 136.997-111.043 248-248 248S8 392.997 8 256C8 119.083 119.043 8 256 8s248 111.083 248 248zM262.655 90c-54.497 0-89.255 22.957-116.549 63.758-3.536 5.286-2.353 12.415 2.715 16.258l34.699 26.31c5.205 3.947 12.621 3.008 16.665-2.122 17.864-22.658 30.113-35.797 57.303-35.797 20.429 0 45.698 13.148 45.698 32.958 0 14.976-12.363 22.667-32.534 33.976C247.128 238.528 216 254.941 216 296v4c0 6.627 5.373 12 12 12h56c6.627 0 12-5.373 12-12v-1.333c0-28.462 83.186-29.647 83.186-106.667 0-58.002-60.165-102-116.531-102zM256 338c-25.365 0-46 20.635-46 46 0 25.364 20.635 46 46 46s46-20.636 46-46c0-25.365-20.635-46-46-46z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>
<br />
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <span class="pf-v6-c-form-control">
      <input
        type="text"
        id="textInput12"
        name="textInput12"
        aria-label="Input example with popover"
      />
    </span>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-plain">
    <button
      class="pf-v6-c-button pf-m-plain"
      type="button"
      aria-label="Popover for input"
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
            d="M504 256c0 136.997-111.043 248-248 248S8 392.997 8 256C8 119.083 119.043 8 256 8s248 111.083 248 248zM262.655 90c-54.497 0-89.255 22.957-116.549 63.758-3.536 5.286-2.353 12.415 2.715 16.258l34.699 26.31c5.205 3.947 12.621 3.008 16.665-2.122 17.864-22.658 30.113-35.797 57.303-35.797 20.429 0 45.698 13.148 45.698 32.958 0 14.976-12.363 22.667-32.534 33.976C247.128 238.528 216 254.941 216 296v4c0 6.627 5.373 12 12 12h56c6.627 0 12-5.373 12-12v-1.333c0-28.462 83.186-29.647 83.186-106.667 0-58.002-60.165-102-116.531-102zM256 338c-25.365 0-46 20.635-46 46 0 25.364 20.635 46 46 46s46-20.636 46-46c0-25.365-20.635-46-46-46z"
          />
        </svg>
      </span>
    </button>
  </div>
</div>
<br />
<div class="pf-v6-c-input-group">
  <div class="pf-v6-c-input-group__item pf-m-fill">
    <span class="pf-v6-c-form-control">
      <input
        type="number"
        id="textInput14"
        name="textInput14"
        aria-label="Input example with plain unit"
      />
    </span>
  </div>
  <div class="pf-v6-c-input-group__item pf-m-plain pf-m-box">
    <span class="pf-v6-c-input-group__text">%</span>
  </div>
</div>

```

## Documentation

### Accessibility

When using the `.pf-v6-c-input-group` always ensure labels are used outside the input group with the `.pf-v6-screen-reader` class applied. You can also make use of the `aria-describedby`, `aria-label`, or `aria-labelledby` attributes. For more information on accessibility and forms see the [form component](/components/forms/form).

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `aria-describedby` | `.pf-v6-c-form-control` |  When using `.pf-v6-c-input-group__text` or `.pf-v6-c-input-group__action` make use of this on the input field. |

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-input-group` | `<div>` |  Initiates the input group. **Required** |
| `.pf-v6-c-input-group__item` | `<div>` |  Initiates the input group item. |
| `.pf-v6-c-input-group__text` | `<span>` |  Initiates input group text. This should be used within `.pf-v6-c-input-group__item` to contain text. |
| `.pf-m-plain` | `.pf-v6-c-input-group__item` | Removes the border from the input group element. |
| `.pf-m-box` | `.pf-v6-c-input-group__item` | Adds appropriate styling for items that are not form controls. |
| `.pf-m-fill` | `.pf-v6-c-input-group__item` | Allows the input group element to stretch to fill available space. |
| `.pf-m-disabled` | `.pf-v6-c-input-group__item` | Adds disabled styling to match a disabled input within the input group. |
| `.pf-m-search-expandable` | `.pf-v6-c-input-group` | Modifies an input group to be an expandable search input. **Note:** The expandable search input can be found in the [search input](/components/search-input/) component docs for react and [text input group](/components/text-input-group/html#search-input-group-expandable) component docs for core. |
| `.pf-m-search-input` | `.pf-v6-c-input-group__item` | Identifies the text input an expandable search input. |
| `.pf-m-search-expand` | `.pf-v6-c-input-group__item` | Identifies the expand button in an expandable search input. |
| `.pf-m-search-action` | `.pf-v6-c-input-group__item` | Identifies actions adjacent to the search input when an expandable search input is expanded. |
