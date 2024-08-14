/**
 * @typedef {Object} ApplicationDef
 * @property {string} tag_name Component tag name
 * @property {string[]} scripts List of script urls
 * @property {string[]} styles List of style urls
 * @property {Record<string, string>} inputs Mapping of model properties to attribute names
 * @property {string[]} outputs List of events to listen to
 */

/** @typedef {{ _application: ApplicationDef } & Record<string, unknown>} Model */

/** @type {(keys: string[], cond: (key: string) => boolean, factory: (key: string) => HTMLElement) => Promise<void>} */
async function loadMetadata(keys, cond, factory) {
  /** @type {Promise<unknown>[]} */
  const promises = [];
  for (const key of keys) {
    if (cond(key)) {
      promises.push(
        new Promise((resolve, reject) => {
          const el = factory(key);
          el.addEventListener('load', resolve);
          el.addEventListener('error', reject);
          document.head.appendChild(el);
        })
      );
    }
  }

  await Promise.all(promises);
}

/** @type {(url: string) => HTMLScriptElement} */
function createScriptElement(url) {
  const el = document.createElement('script');
  el.src = url;
  el.defer = true;
  return el;
}

/** @type {(url: string) => HTMLLinkElement} */
function createStyleElement(url) {
  const el = document.createElement('link');
  el.href = url;
  el.rel = 'stylesheet';
  return el;
}

/** @type {import("npm:@anywidget/types").Initialize<Model>} */
async function initialize({ model }) {
  const application = model.get('_application');
  await Promise.all([
    loadMetadata(
      application.scripts,
      (url) => document.querySelector(`script[src="${url}"]`) === null,
      createScriptElement
    ),
    loadMetadata(
      application.styles,
      (url) => document.querySelector(`link[href="${url}"]`) === null,
      createStyleElement
    ),
  ]);
}

/** @type {(model: import("npm:@anywidget/types").AnyModel<Model>, instance: HTMLElement, key: string, attr: string) => void} */
function updateAttribute(model, instance, key, attr) {
  let value = model.get(key);
  if (value === null) {
    instance.removeAttribute(attr);
    return;
  }

  if (typeof value !== 'string') {
    value = JSON.stringify(value);
  }

  instance.setAttribute(attr, /** @type {string} */ (value));
}

/** @type {(model: import("npm:@anywidget/types").AnyModel<Model>, instance: HTMLElement, eventName: string) => void} */
function registerEvent(model, instance, eventName) {
  instance.addEventListener(eventName, (event) => {
    const data = /** @type {CustomEvent} */ (event).detail;
    model.send({ event: eventName, data });
  });
}

/** @type {import("npm:@anywidget/types").Render<Model>} */
async function render({ model, el }) {
  const application = model.get('_application');
  const instance = document.createElement(application.tag_name);

  for (const [key, attr] of Object.entries(application.inputs)) {
    const update = updateAttribute.bind(null, model, instance, key, attr);
    update();
    model.on(`change:${key}`, update);
  }

  for (const eventName of application.outputs) {
    registerEvent(model, instance, eventName);
  }

  el.append(instance);

  // TODO improve
  await new Promise((r) => setTimeout(r, 1000));
}

export default { initialize, render };
