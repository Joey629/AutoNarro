---
id: 'Dual list selector'
section: components
cssPrefix: pf-v6-c-dual-list-selector
---## Examples

### Basic

```html
<div class="pf-v6-c-dual-list-selector">
  <div class="pf-v6-c-dual-list-selector__pane pf-m-available">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Available options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="basic-available-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="basic-available-status-text"
      >0 of 5 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="basic-available-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item1</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item2</span>
              </span>
            </span>
          </div>
        </li>
        <li
          class="pf-v6-c-dual-list-selector__list-item pf-m-disabled"
          role="option"
        >
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                >Item3 (disabled)</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item4</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item5</span>
              </span>
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__controls">
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Add selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Add all"
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
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove all"
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
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__pane pf-m-chosen">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Chosen options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="basic-chosen-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="basic-chosen-status-text"
      >0 of 0 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="basic-chosen-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      ></ul>
    </div>
  </div>
</div>

```

### Available item selected

```html
<div class="pf-v6-c-dual-list-selector">
  <div class="pf-v6-c-dual-list-selector__pane pf-m-available">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Available options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="available-item-selected-available-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="available-item-selected-available-status-text"
      >1 of 5 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="available-item-selected-available-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item1</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-selected">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item2</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item3</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item4</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item5</span>
              </span>
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__controls">
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Add selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Add all"
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
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove all"
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
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__pane pf-m-chosen">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Chosen options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="available-item-selected-chosen-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="available-item-selected-chosen-status-text"
      >0 of 0 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="available-item-selected-chosen-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      ></ul>
    </div>
  </div>
</div>

```

### Multiple available items selected

```html
<div class="pf-v6-c-dual-list-selector">
  <div class="pf-v6-c-dual-list-selector__pane pf-m-available">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Available options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="multiple-available-items-selected-available-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="multiple-available-items-selected-available-status-text"
      >3 of 5 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="multiple-available-items-selected-available-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item1</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-selected">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item2</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-selected">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item3</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item4</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-selected">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item5</span>
              </span>
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__controls">
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Add selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Add all"
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
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove all"
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
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__pane pf-m-chosen">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Chosen options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="multiple-available-items-selected-chosen-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="multiple-available-items-selected-chosen-status-text"
      >0 of 0 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="multiple-available-items-selected-chosen-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      ></ul>
    </div>
  </div>
</div>

```

### Chosen item

```html
<div class="pf-v6-c-dual-list-selector">
  <div class="pf-v6-c-dual-list-selector__pane pf-m-available">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Available options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="chosen-item-available-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="chosen-item-available-status-text"
      >0 of 4 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="chosen-item-available-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item1</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item2</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item3</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item4</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item5</span>
              </span>
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__controls">
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Add selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Add all"
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
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Remove all"
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
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__pane pf-m-chosen">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Chosen options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="chosen-item-chosen-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="chosen-item-chosen-status-text"
      >0 of 1 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="chosen-item-chosen-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item1</span>
              </span>
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</div>

```

### Chosen item selected

```html
<div class="pf-v6-c-dual-list-selector">
  <div class="pf-v6-c-dual-list-selector__pane pf-m-available">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Available options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="chosen-item-selected-available-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="chosen-item-selected-available-status-text"
      >0 of 4 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="chosen-item-selected-available-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item1</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item2</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item3</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item4</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item5</span>
              </span>
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__controls">
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Add selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Add all"
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
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Remove all"
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
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Remove selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__pane pf-m-chosen">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Chosen options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="chosen-item-selected-chosen-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="chosen-item-selected-chosen-status-text"
      >1 of 1 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="chosen-item-selected-chosen-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-selected">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item5</span>
              </span>
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</div>

```

### Tree view

```html
<div class="pf-v6-c-dual-list-selector">
  <div class="pf-v6-c-dual-list-selector__pane pf-m-available">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Available options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="tree-available-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="tree-available-status-text"
      >1 of 11 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="tree"
        aria-labelledby="tree-available-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li
          class="pf-v6-c-dual-list-selector__list-item pf-m-expandable pf-m-expanded"
          aria-expanded="true"
          role="treeitem"
        >
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <div class="pf-v6-c-dual-list-selector__item-toggle">
                  <span class="pf-v6-c-dual-list-selector__item-toggle-icon">
                    <svg
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
                </div>
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-0"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span class="pf-v6-c-dual-list-selector__item-text">Colors</span>
              </span>
              <span class="pf-v6-c-dual-list-selector__item-count">
                <span class="pf-v6-c-badge pf-m-read">6</span>
              </span>
            </div>
          </div>

          <ul
            class="pf-v6-c-dual-list-selector__list"
            role="group"
            aria-labelledby="-status-text"
          >
            <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
              <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
                <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          id="check-1"
                          aria-label="Dual list selector item check"
                        />
                      </div>
                    </span>
                    <span class="pf-v6-c-dual-list-selector__item-text">Red</span>
                  </span>
                </div>
              </div>
            </li>
            <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
              <div
                class="pf-v6-c-dual-list-selector__list-item-row pf-m-check pf-m-selected"
              >
                <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          id="check-2"
                          checked
                          aria-label="Dual list selector item check checked"
                        />
                      </div>
                    </span>
                    <span class="pf-v6-c-dual-list-selector__item-text">Orange</span>
                  </span>
                </div>
              </div>
            </li>
            <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
              <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
                <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          id="check-3"
                          aria-label="Dual list selector item check"
                        />
                      </div>
                    </span>
                    <span class="pf-v6-c-dual-list-selector__item-text">Yellow</span>
                  </span>
                </div>
              </div>
            </li>
            <li
              class="pf-v6-c-dual-list-selector__list-item pf-m-expandable pf-m-expanded"
              aria-expanded="true"
              role="treeitem"
            >
              <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
                <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <div class="pf-v6-c-dual-list-selector__item-toggle">
                      <span
                        class="pf-v6-c-dual-list-selector__item-toggle-icon"
                      >
                        <svg
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
                    </div>
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          id="check-4"
                          aria-label="Dual list selector item check"
                        />
                      </div>
                    </span>
                    <span class="pf-v6-c-dual-list-selector__item-text">Green</span>
                  </span>
                </div>
              </div>

              <ul
                class="pf-v6-c-dual-list-selector__list"
                role="group"
                aria-labelledby="-status-text"
              >
                <li
                  class="pf-v6-c-dual-list-selector__list-item"
                  role="treeitem"
                >
                  <div
                    class="pf-v6-c-dual-list-selector__list-item-row pf-m-check"
                  >
                    <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                      <span class="pf-v6-c-dual-list-selector__item-main">
                        <span class="pf-v6-c-dual-list-selector__item-check">
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="check-5"
                              aria-label="Dual list selector item check"
                            />
                          </div>
                        </span>
                        <span
                          class="pf-v6-c-dual-list-selector__item-text"
                        >Light green</span>
                      </span>
                    </div>
                  </div>
                </li>
                <li
                  class="pf-v6-c-dual-list-selector__list-item"
                  role="treeitem"
                >
                  <div
                    class="pf-v6-c-dual-list-selector__list-item-row pf-m-check"
                  >
                    <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                      <span class="pf-v6-c-dual-list-selector__item-main">
                        <span class="pf-v6-c-dual-list-selector__item-check">
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="check-6"
                              aria-label="Dual list selector item check"
                            />
                          </div>
                        </span>
                        <span
                          class="pf-v6-c-dual-list-selector__item-text"
                        >Medium green</span>
                      </span>
                    </div>
                  </div>
                </li>
                <li
                  class="pf-v6-c-dual-list-selector__list-item"
                  role="treeitem"
                >
                  <div
                    class="pf-v6-c-dual-list-selector__list-item-row pf-m-check"
                  >
                    <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                      <span class="pf-v6-c-dual-list-selector__item-main">
                        <span class="pf-v6-c-dual-list-selector__item-check">
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="check-7"
                              aria-label="Dual list selector item check"
                            />
                          </div>
                        </span>
                        <span
                          class="pf-v6-c-dual-list-selector__item-text"
                        >Dark green</span>
                      </span>
                    </div>
                  </div>
                </li>
              </ul>
            </li>
          </ul>
        </li>

        <li
          class="pf-v6-c-dual-list-selector__list-item pf-m-expandable"
          aria-expanded="true"
          role="treeitem"
        >
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <div class="pf-v6-c-dual-list-selector__item-toggle">
                  <span class="pf-v6-c-dual-list-selector__item-toggle-icon">
                    <svg
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
                </div>
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-8"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                >Type something</span>
              </span>
            </div>
          </div>
        </li>

        <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-9"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                >Type something</span>
              </span>
            </div>
          </div>
        </li>

        <li
          class="pf-v6-c-dual-list-selector__list-item pf-m-expandable"
          aria-expanded="true"
          role="treeitem"
        >
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <div class="pf-v6-c-dual-list-selector__item-toggle">
                  <span class="pf-v6-c-dual-list-selector__item-toggle-icon">
                    <svg
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
                </div>
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-10"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                >Type something</span>
              </span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__controls">
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Add selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Add all"
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
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove all"
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
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__pane pf-m-chosen">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Chosen options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="tree-chosen-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="tree-chosen-status-text"
      >0 of 0 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="tree-chosen-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      ></ul>
    </div>
  </div>
</div>

```

### Tree view with chosen and disabled options

```html
<div class="pf-v6-c-dual-list-selector">
  <div class="pf-v6-c-dual-list-selector__pane pf-m-available">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Available options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="tree-options-available-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="tree-options-available-status-text"
      >0 of 10 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="tree"
        aria-labelledby="tree-options-available-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li
          class="pf-v6-c-dual-list-selector__list-item pf-m-expandable pf-m-expanded"
          aria-expanded="true"
          role="treeitem"
        >
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <div class="pf-v6-c-dual-list-selector__item-toggle">
                  <span class="pf-v6-c-dual-list-selector__item-toggle-icon">
                    <svg
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
                </div>
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-11"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span class="pf-v6-c-dual-list-selector__item-text">Colors</span>
              </span>
              <span class="pf-v6-c-dual-list-selector__item-count">
                <span class="pf-v6-c-badge pf-m-read">6</span>
              </span>
            </div>
          </div>

          <ul
            class="pf-v6-c-dual-list-selector__list"
            role="group"
            aria-labelledby="-status-text"
          >
            <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
              <div
                class="pf-v6-c-dual-list-selector__list-item-row pf-m-check pf-m-selected"
              >
                <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          id="check-12"
                          checked
                          aria-label="Dual list selector item check checked"
                        />
                      </div>
                    </span>
                    <span class="pf-v6-c-dual-list-selector__item-text">Orange</span>
                  </span>
                </div>
              </div>
            </li>
            <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
              <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
                <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          id="check-13"
                          aria-label="Dual list selector item check"
                        />
                      </div>
                    </span>
                    <span class="pf-v6-c-dual-list-selector__item-text">Yellow</span>
                  </span>
                </div>
              </div>
            </li>
            <li
              class="pf-v6-c-dual-list-selector__list-item pf-m-expandable pf-m-expanded pf-m-disabled"
              aria-expanded="true"
              role="treeitem"
            >
              <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
                <div class="pf-v6-c-dual-list-selector__item">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <div class="pf-v6-c-dual-list-selector__item-toggle">
                      <span
                        class="pf-v6-c-dual-list-selector__item-toggle-icon"
                      >
                        <svg
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
                    </div>
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          disabled
                          id="check-14"
                          aria-label="Dual list selector item check"
                        />
                      </div>
                    </span>
                    <span
                      class="pf-v6-c-dual-list-selector__item-text"
                    >Green (disabled)</span>
                  </span>
                </div>
              </div>

              <ul
                class="pf-v6-c-dual-list-selector__list"
                role="group"
                aria-labelledby="-status-text"
              >
                <li
                  class="pf-v6-c-dual-list-selector__list-item"
                  role="treeitem"
                >
                  <div
                    class="pf-v6-c-dual-list-selector__list-item-row pf-m-check"
                  >
                    <div class="pf-v6-c-dual-list-selector__item">
                      <span class="pf-v6-c-dual-list-selector__item-main">
                        <span class="pf-v6-c-dual-list-selector__item-check">
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              disabled
                              id="check-15"
                              aria-label="Dual list selector item check"
                            />
                          </div>
                        </span>
                        <span
                          class="pf-v6-c-dual-list-selector__item-text"
                        >Light green</span>
                      </span>
                    </div>
                  </div>
                </li>
                <li
                  class="pf-v6-c-dual-list-selector__list-item"
                  role="treeitem"
                >
                  <div
                    class="pf-v6-c-dual-list-selector__list-item-row pf-m-check"
                  >
                    <div class="pf-v6-c-dual-list-selector__item">
                      <span class="pf-v6-c-dual-list-selector__item-main">
                        <span class="pf-v6-c-dual-list-selector__item-check">
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              disabled
                              id="check-16"
                              aria-label="Dual list selector item check"
                            />
                          </div>
                        </span>
                        <span
                          class="pf-v6-c-dual-list-selector__item-text"
                        >Medium green</span>
                      </span>
                    </div>
                  </div>
                </li>
                <li
                  class="pf-v6-c-dual-list-selector__list-item"
                  role="treeitem"
                >
                  <div
                    class="pf-v6-c-dual-list-selector__list-item-row pf-m-check"
                  >
                    <div class="pf-v6-c-dual-list-selector__item">
                      <span class="pf-v6-c-dual-list-selector__item-main">
                        <span class="pf-v6-c-dual-list-selector__item-check">
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              disabled
                              id="check-17"
                              aria-label="Dual list selector item check"
                            />
                          </div>
                        </span>
                        <span
                          class="pf-v6-c-dual-list-selector__item-text"
                        >Dark green</span>
                      </span>
                    </div>
                  </div>
                </li>
              </ul>
            </li>
          </ul>
        </li>
        <li
          class="pf-v6-c-dual-list-selector__list-item pf-m-expandable"
          aria-expanded="true"
          role="treeitem"
        >
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <div class="pf-v6-c-dual-list-selector__item-toggle">
                  <span class="pf-v6-c-dual-list-selector__item-toggle-icon">
                    <svg
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
                </div>
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-18"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                >Type something</span>
              </span>
            </div>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-19"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                >Type something</span>
              </span>
            </div>
          </div>
        </li>
        <li
          class="pf-v6-c-dual-list-selector__list-item pf-m-expandable"
          aria-expanded="true"
          role="treeitem"
        >
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <div class="pf-v6-c-dual-list-selector__item-toggle">
                  <span class="pf-v6-c-dual-list-selector__item-toggle-icon">
                    <svg
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
                </div>
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-20"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                >Type something</span>
              </span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__controls">
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Add selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Add all"
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
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove all"
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
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__pane pf-m-chosen">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Chosen options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="tree-options-chosen-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="tree-options-chosen-status-text"
      >0 of 0 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="tree"
        aria-labelledby="tree-options-chosen-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li
          class="pf-v6-c-dual-list-selector__list-item pf-m-expandable pf-m-expanded"
          aria-expanded="true"
          role="treeitem"
        >
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <div class="pf-v6-c-dual-list-selector__item-toggle">
                  <span class="pf-v6-c-dual-list-selector__item-toggle-icon">
                    <svg
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
                </div>
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-21"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span class="pf-v6-c-dual-list-selector__item-text">Colors</span>
              </span>
            </div>
          </div>

          <ul
            class="pf-v6-c-dual-list-selector__list"
            role="group"
            aria-labelledby="-status-text"
          >
            <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
              <div
                class="pf-v6-c-dual-list-selector__list-item-row pf-m-check pf-m-selected"
              >
                <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          id="check-22"
                          checked
                          aria-label="Dual list selector item check checked"
                        />
                      </div>
                    </span>
                    <span class="pf-v6-c-dual-list-selector__item-text">Orange</span>
                  </span>
                </div>
              </div>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</div>

```

### Tree view animated

```html
<div class="pf-v6-c-dual-list-selector pf-m-animate-expand">
  <div class="pf-v6-c-dual-list-selector__pane pf-m-available">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Available options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="tree-available-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="tree-available-status-text"
      >1 of 11 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="tree"
        aria-labelledby="tree-available-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li
          class="pf-v6-c-dual-list-selector__list-item pf-m-expandable pf-m-expanded"
          aria-expanded="true"
          role="treeitem"
        >
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <div class="pf-v6-c-dual-list-selector__item-toggle">
                  <span class="pf-v6-c-dual-list-selector__item-toggle-icon">
                    <svg
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
                </div>
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-0"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span class="pf-v6-c-dual-list-selector__item-text">Colors</span>
              </span>
              <span class="pf-v6-c-dual-list-selector__item-count">
                <span class="pf-v6-c-badge pf-m-read">6</span>
              </span>
            </div>
          </div>

          <ul
            class="pf-v6-c-dual-list-selector__list"
            role="group"
            aria-labelledby="-status-text"
          >
            <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
              <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
                <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          id="check-1"
                          aria-label="Dual list selector item check"
                        />
                      </div>
                    </span>
                    <span class="pf-v6-c-dual-list-selector__item-text">Red</span>
                  </span>
                </div>
              </div>
            </li>
            <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
              <div
                class="pf-v6-c-dual-list-selector__list-item-row pf-m-check pf-m-selected"
              >
                <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          id="check-2"
                          checked
                          aria-label="Dual list selector item check checked"
                        />
                      </div>
                    </span>
                    <span class="pf-v6-c-dual-list-selector__item-text">Orange</span>
                  </span>
                </div>
              </div>
            </li>
            <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
              <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
                <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          id="check-3"
                          aria-label="Dual list selector item check"
                        />
                      </div>
                    </span>
                    <span class="pf-v6-c-dual-list-selector__item-text">Yellow</span>
                  </span>
                </div>
              </div>
            </li>
            <li
              class="pf-v6-c-dual-list-selector__list-item pf-m-expandable pf-m-expanded"
              aria-expanded="true"
              role="treeitem"
            >
              <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
                <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                  <span class="pf-v6-c-dual-list-selector__item-main">
                    <div class="pf-v6-c-dual-list-selector__item-toggle">
                      <span
                        class="pf-v6-c-dual-list-selector__item-toggle-icon"
                      >
                        <svg
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
                    </div>
                    <span class="pf-v6-c-dual-list-selector__item-check">
                      <div class="pf-v6-c-check pf-m-standalone">
                        <input
                          class="pf-v6-c-check__input"
                          type="checkbox"
                          id="check-4"
                          aria-label="Dual list selector item check"
                        />
                      </div>
                    </span>
                    <span class="pf-v6-c-dual-list-selector__item-text">Green</span>
                  </span>
                </div>
              </div>

              <ul
                class="pf-v6-c-dual-list-selector__list"
                role="group"
                aria-labelledby="-status-text"
              >
                <li
                  class="pf-v6-c-dual-list-selector__list-item"
                  role="treeitem"
                >
                  <div
                    class="pf-v6-c-dual-list-selector__list-item-row pf-m-check"
                  >
                    <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                      <span class="pf-v6-c-dual-list-selector__item-main">
                        <span class="pf-v6-c-dual-list-selector__item-check">
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="check-5"
                              aria-label="Dual list selector item check"
                            />
                          </div>
                        </span>
                        <span
                          class="pf-v6-c-dual-list-selector__item-text"
                        >Light green</span>
                      </span>
                    </div>
                  </div>
                </li>
                <li
                  class="pf-v6-c-dual-list-selector__list-item"
                  role="treeitem"
                >
                  <div
                    class="pf-v6-c-dual-list-selector__list-item-row pf-m-check"
                  >
                    <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                      <span class="pf-v6-c-dual-list-selector__item-main">
                        <span class="pf-v6-c-dual-list-selector__item-check">
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="check-6"
                              aria-label="Dual list selector item check"
                            />
                          </div>
                        </span>
                        <span
                          class="pf-v6-c-dual-list-selector__item-text"
                        >Medium green</span>
                      </span>
                    </div>
                  </div>
                </li>
                <li
                  class="pf-v6-c-dual-list-selector__list-item"
                  role="treeitem"
                >
                  <div
                    class="pf-v6-c-dual-list-selector__list-item-row pf-m-check"
                  >
                    <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
                      <span class="pf-v6-c-dual-list-selector__item-main">
                        <span class="pf-v6-c-dual-list-selector__item-check">
                          <div class="pf-v6-c-check pf-m-standalone">
                            <input
                              class="pf-v6-c-check__input"
                              type="checkbox"
                              id="check-7"
                              aria-label="Dual list selector item check"
                            />
                          </div>
                        </span>
                        <span
                          class="pf-v6-c-dual-list-selector__item-text"
                        >Dark green</span>
                      </span>
                    </div>
                  </div>
                </li>
              </ul>
            </li>
          </ul>
        </li>

        <li
          class="pf-v6-c-dual-list-selector__list-item pf-m-expandable"
          aria-expanded="true"
          role="treeitem"
        >
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <div class="pf-v6-c-dual-list-selector__item-toggle">
                  <span class="pf-v6-c-dual-list-selector__item-toggle-icon">
                    <svg
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
                </div>
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-8"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                >Type something</span>
              </span>
            </div>
          </div>
        </li>

        <li class="pf-v6-c-dual-list-selector__list-item" role="treeitem">
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-9"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                >Type something</span>
              </span>
            </div>
          </div>
        </li>

        <li
          class="pf-v6-c-dual-list-selector__list-item pf-m-expandable"
          aria-expanded="true"
          role="treeitem"
        >
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-check">
            <div class="pf-v6-c-dual-list-selector__item" tabindex="0">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <div class="pf-v6-c-dual-list-selector__item-toggle">
                  <span class="pf-v6-c-dual-list-selector__item-toggle-icon">
                    <svg
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
                </div>
                <span class="pf-v6-c-dual-list-selector__item-check">
                  <div class="pf-v6-c-check pf-m-standalone">
                    <input
                      class="pf-v6-c-check__input"
                      type="checkbox"
                      id="check-10"
                      aria-label="Dual list selector item check"
                    />
                  </div>
                </span>
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                >Type something</span>
              </span>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__controls">
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Add selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Add all"
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
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove all"
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
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__pane pf-m-chosen">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Chosen options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="tree-chosen-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="tree-chosen-status-text"
      >0 of 0 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="tree-chosen-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      ></ul>
    </div>
  </div>
</div>

```

### Draggable

```html
<div
  id="draggable-help"
>Activate the reorder button and use the arrow keys to reorder the list or use your mouse to drag/reorder. Press escape to cancel the reordering.</div>
<div class="pf-v6-c-dual-list-selector">
  <div class="pf-v6-c-dual-list-selector__pane pf-m-available">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Available options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="draggable-available-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="draggable-available-status-text"
      >0 of 5 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="draggable-available-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item1</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item4</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span class="pf-v6-c-dual-list-selector__item-text">Item6</span>
              </span>
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__controls">
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Add selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Add all"
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
              d="M224.3 273l-136 136c-9.4 9.4-24.6 9.4-33.9 0l-22.6-22.6c-9.4-9.4-9.4-24.6 0-33.9l96.4-96.4-96.4-96.4c-9.4-9.4-9.4-24.6 0-33.9L54.3 103c9.4-9.4 24.6-9.4 33.9 0l136 136c9.5 9.4 9.5 24.6.1 34zm192-34l-136-136c-9.4-9.4-24.6-9.4-33.9 0l-22.6 22.6c-9.4 9.4-9.4 24.6 0 33.9l96.4 96.4-96.4 96.4c-9.4 9.4-9.4 24.6 0 33.9l22.6 22.6c9.4 9.4 24.6 9.4 33.9 0l136-136c9.4-9.2 9.4-24.4 0-33.8z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove all"
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
              d="M223.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L319.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L393.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34zm-192 34l136 136c9.4 9.4 24.6 9.4 33.9 0l22.6-22.6c9.4-9.4 9.4-24.6 0-33.9L127.9 256l96.4-96.4c9.4-9.4 9.4-24.6 0-33.9L201.7 103c-9.4-9.4-24.6-9.4-33.9 0l-136 136c-9.5 9.4-9.5 24.6-.1 34z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div class="pf-v6-c-dual-list-selector__controls-item">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        disabled
        aria-label="Remove selected"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 256 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M31.7 239l136-136c9.4-9.4 24.6-9.4 33.9 0l22.6 22.6c9.4 9.4 9.4 24.6 0 33.9L127.9 256l96.4 96.4c9.4 9.4 9.4 24.6 0 33.9L201.7 409c-9.4 9.4-24.6 9.4-33.9 0l-136-136c-9.5-9.4-9.5-24.6-.1-34z"
            />
          </svg>
        </span>
      </button>
    </div>
  </div>
  <div class="pf-v6-c-dual-list-selector__pane pf-m-chosen">
    <div class="pf-v6-c-dual-list-selector__header">
      <div class="pf-v6-c-dual-list-selector__title">
        <div class="pf-v6-c-dual-list-selector__title-text">Chosen options</div>
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__tools">
      <div class="pf-v6-c-dual-list-selector__tools-filter">
        <div class="pf-v6-c-text-input-group">
          <div class="pf-v6-c-text-input-group__main pf-m-icon">
            <span class="pf-v6-c-text-input-group__text">
              <span class="pf-v6-c-text-input-group__icon">
                <i class="fas fa-fw fa-search"></i>
              </span>
              <input
                class="pf-v6-c-text-input-group__text-input"
                type="text"
                value
                aria-label="Search input"
              />
            </span>
          </div>
        </div>
      </div>
      <div class="pf-v6-c-dual-list-selector__tools-actions">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Sort"
        >
          <span class="pf-v6-c-button__icon">
            <span class="pf-v6-c-icon">
              <span class="pf-v6-c-icon__content pf-v6-m-mirror-inline-rtl">
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
                    d="M304 416h-64a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h64a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-128-64h-48V48a16 16 0 0 0-16-16H80a16 16 0 0 0-16 16v304H16c-14.19 0-21.37 17.24-11.29 27.31l80 96a16 16 0 0 0 22.62 0l80-96C197.35 369.26 190.22 352 176 352zm256-192H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h192a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zm-64 128H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h128a16 16 0 0 0 16-16v-32a16 16 0 0 0-16-16zM496 32H240a16 16 0 0 0-16 16v32a16 16 0 0 0 16 16h256a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16z"
                  />
                </svg>
              </span>
            </span>
          </span>
        </button>
        <button
          class="pf-v6-c-menu-toggle pf-m-plain"
          type="button"
          aria-expanded="false"
          aria-label="Dual list item menu toggle"
          id="draggable-chosen-menu-toggle"
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
      </div>
    </div>
    <div class="pf-v6-c-dual-list-selector__status">
      <span
        class="pf-v6-c-dual-list-selector__status-text"
        id="draggable-chosen-status-text"
      >0 of 0 items selected</span>
    </div>
    <div class="pf-v6-c-dual-list-selector__menu" tabindex="0">
      <ul
        class="pf-v6-c-dual-list-selector__list"
        role="listbox"
        aria-labelledby="draggable-chosen-status-text"
        aria-multiselectable="true"
        aria-activedescendant
      >
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <div class="pf-v6-c-dual-list-selector__draggable">
              <span class="pf-v6-c-button pf-m-plain pf-m-disabled">
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
                      d="M96 32H32C14.33 32 0 46.33 0 64v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32V64c0-17.67-14.33-32-32-32zm0 160H32c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zm0 160H32c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zM288 32h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32V64c0-17.67-14.33-32-32-32zm0 160h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zm0 160h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32z"
                    />
                  </svg>
                </span>
              </span>
            </div>
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                  id="draggable-list-item-2-item-text"
                >Item2 - draggable icon disabled</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row">
            <div class="pf-v6-c-dual-list-selector__draggable">
              <span class="pf-v6-c-button pf-m-plain">
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
                      d="M96 32H32C14.33 32 0 46.33 0 64v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32V64c0-17.67-14.33-32-32-32zm0 160H32c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zm0 160H32c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zM288 32h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32V64c0-17.67-14.33-32-32-32zm0 160h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zm0 160h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32z"
                    />
                  </svg>
                </span>
              </span>
            </div>
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                  id="draggable-list-item-3-item-text"
                >Item3</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-ghost-row">
            <div class="pf-v6-c-dual-list-selector__draggable">
              <span class="pf-v6-c-button pf-m-plain pf-m-disabled">
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
                      d="M96 32H32C14.33 32 0 46.33 0 64v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32V64c0-17.67-14.33-32-32-32zm0 160H32c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zm0 160H32c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zM288 32h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32V64c0-17.67-14.33-32-32-32zm0 160h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zm0 160h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32z"
                    />
                  </svg>
                </span>
              </span>
            </div>
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                  id="draggable-list-item-5-item-text"
                >Item5 - ghost row</span>
              </span>
            </span>
          </div>
        </li>
        <li class="pf-v6-c-dual-list-selector__list-item" role="option">
          <div class="pf-v6-c-dual-list-selector__list-item-row pf-m-selected">
            <div class="pf-v6-c-dual-list-selector__draggable">
              <span class="pf-v6-c-button pf-m-plain">
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
                      d="M96 32H32C14.33 32 0 46.33 0 64v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32V64c0-17.67-14.33-32-32-32zm0 160H32c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zm0 160H32c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zM288 32h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32V64c0-17.67-14.33-32-32-32zm0 160h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32zm0 160h-64c-17.67 0-32 14.33-32 32v64c0 17.67 14.33 32 32 32h64c17.67 0 32-14.33 32-32v-64c0-17.67-14.33-32-32-32z"
                    />
                  </svg>
                </span>
              </span>
            </div>
            <span class="pf-v6-c-dual-list-selector__item">
              <span class="pf-v6-c-dual-list-selector__item-main">
                <span
                  class="pf-v6-c-dual-list-selector__item-text"
                  id="draggable-list-item-7-item-text"
                >Item7 - selected</span>
              </span>
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</div>
<div
  class="pf-v6-screen-reader"
  aria-live="assertive"
>This is the aria-live section that provides real-time feedback to the user.</div>

```

## Documentation

### Accessibility

| Attribute | Applied to | Outcome |
| -- | -- | -- |
| `aria-live` | `[element with live text]` | To give screen reader users live feedback about what's happening during interaction with the dual list selector, both during drag and drop interactions and keyboard interactions. **Highly Recommended** |
| `aria-labelledby="[id of .pf-v6-c-dual-list-selector__status-text]` | `.pf-v6-c-dual-list-selector__list [ul]` | Gives the list an accessible name. |
| `role="listbox or tree or group"` | `.pf-v6-c-dual-list-selector__list [ul]` | Indicates the list is single, a tree, or a subgroup within the tree. |
| `aria-multiselectable="true"` | `.pf-v6-c-dual-list-selector__list [ul]` | Indicates the list is multiselectable. |
| `aria-activedescendant=""` | `.pf-v6-c-dual-list-selector__list [ul]` | Indicates the list has clickable children. |
| `role="option or treeitem"` | `.pf-v6-c-dual-list-selector__list-item [li]` | Indicates whether the item is part of a tree. |
| `aria-expanded="true"`      | `.pf-v6-c-dual-list-selector__list-item [li]` | Indicates a treeitem is expanded. |

### Usage

| Class | Applied | Outcome |
| -- | -- | -- |
| `.pf-v6-c-dual-list-selector` | `<div>` | Initiates the dual list selector component. **Required** |
| `.pf-v6-c-dual-list-selector__pane` | `<div>` | Initiates a dual list selector pane. **Required** |
| `.pf-v6-c-dual-list-selector__header` | `<div>` | Initiates a dual list selector pane header. **Required** |
| `.pf-v6-c-dual-list-selector__title` | `<div>` | Initiates a dual list selector pane title. **Required** |
| `.pf-v6-c-dual-list-selector__title-text` | `<div>` | Initiates a dual list selector pane title text. **Required** |
| `.pf-v6-c-dual-list-selector__tools` | `<div>` | Initiates a dual list selector tools. **Required** |
| `.pf-v6-c-dual-list-selector__filter` | `<div>` | Initiates a dual list selector pane filter. **Required** |
| `.pf-v6-c-dual-list-selector__actions` | `<div>` | Initiates a dual list selector pane actions. |
| `.pf-v6-c-dual-list-selector__actions-item` | `<div>` | Initiates a dual list selector pane actions item. |
| `.pf-v6-c-dual-list-selector__status` | `<div>` | Initiates a dual list selector pane selected status. **Required** |
| `.pf-v6-c-dual-list-selector__status-text` | `<span>` | Initiates a dual list selector pane selected status text. **Required** |
| `.pf-v6-c-dual-list-selector__menu` | `<div>` | Initiates a dual list selector pane menu container. **Required** |
| `.pf-v6-c-dual-list-selector__list` | `<ul>` | Initiates a dual list selector pane menu list. **Required** |
| `.pf-v6-c-dual-list-selector__list-item` | `<li>` | Initiates a dual list selector pane menu list item. **Required** |
| `.pf-v6-c-dual-list-selector__list-item-row` | `<div>` | Initiates a dual list selector pane menu list item row. **Required** |
| `.pf-v6-c-dual-list-selector__draggable` | `<div>` | Initiates a dual list selector pane draggable element. |
| `.pf-v6-c-dual-list-selector__item` | `<span>`, `<div>` | Initiates a dual list selector pane menu item. **Required** |
| `.pf-v6-c-dual-list-selector__item-main` | `<span>` | Initiates a dual list selector pane menu item main container. **Required** |
| `.pf-v6-c-dual-list-selector__item-check` | `<span>` | Initiates the dual list selector item check. |
| `.pf-v6-c-dual-list-selector__item-count` | `<span>` | Initiates the dual list selector item count. |
| `.pf-v6-c-dual-list-selector__item-toggle-icon` | `<span>` | Initiates the dual list selector item toggle icon. |
| `.pf-v6-c-dual-list-selector__item-toggle` | `<button>` | Initiates the dual list selector item toggle. |
| `.pf-v6-c-dual-list-selector__item-text` | `<span>` | Initiates a dual list selector pane menu item text. **Required** |
| `.pf-v6-c-dual-list-selector__controls` | `<div>` | Initiates the dual list selector controls. **Required** |
| `.pf-v6-c-dual-list-selector__controls-item` | `<div>` | Initiates the dual list selector controls item. **Required** |
| `.pf-m-animate-expand` | `.pf-v6-c-dual-list-selector` | Animates the expansion of dual list selector tree view. |
| `.pf-m-available` | `.pf-v6-c-dual-list-selector__pane` | Defines a pane as the available list. |
| `.pf-m-chosen` | `.pf-v6-c-dual-list-selector__pane` | Defines a pane as the chosen list. |
| `.pf-m-drag-over` | `.pf-v6-c-dual-list-selector__list` | Modifies the dual list selector list to indicate that a draggable item is being dragged over the list. |
| `.pf-m-ghost-row` | `.pf-v6-c-dual-list-selector__list-item-row` | Modifies the list item main to be a ghost row. |
| `.pf-m-selected` | `.pf-v6-c-dual-list-selector__list-item-row` | Modifies the menu item for the selected state. |
| `.pf-m-check` | `.pf-v6-c-dual-list-selector__list-item-row` | Indicates that an item is selectable with a checkbox. |
| `.pf-m-expandable` | `.pf-v6-c-dual-list-selector__list-item` | Indicates that an item is expandable. |
| `.pf-m-expanded` | `.pf-v6-c-dual-list-selector__list-item` | Indicates that an item is expanded. |
| `.pf-m-disabled` | `.pf-v6-c-dual-list-selector__list-item` | Indicates that an item is disabled. **Note:** If an item is expandable, only the top level item needs the disabled class. |
